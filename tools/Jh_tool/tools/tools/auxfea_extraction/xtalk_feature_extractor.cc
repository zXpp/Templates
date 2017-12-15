// Copyright (C) 2004 John Dines (John.Dines@idiap.ch)  
//                
// This file is part of Torch 3.
//
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
// 3. The name of the author may not be used to endorse or promote products
//    derived from this software without specific prior written permission.
// 
// THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
// NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

const char *help = "\
Meeting cross-talk detection feature extraction tool\n\
John Dines (c) IDIAP 2005\n\
\n";

// system include files
//
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <math.h>
#include <limits.h>
#include <sys/stat.h>

// fft library
#include <fftw3.h>

// TORCH includes
#include "CmdLine.h"
#include "Allocator.h"
#include "SKListCmdOption.h"
#include "string_utils.h"
#include "IOHTKFeat.h"
#include "log_add.h"

#include "cb.cc"

using namespace Torch;

bool *feat_f;

bool window_f;
bool hpfilter_f;
bool compress_f;
int frame_size;
int frame_shift;
int sample_frequency;
int skip;
//int tau;

SKListCmdOption ref_files( "meeting files .. ", "list of meeting signals                      ");        // input file name list feature set 1

real calc_energy(Circular_buffer *cb);
real calc_kurtosis(Circular_buffer *cb);
real calc_max_xcor(Circular_buffer *cb1, Circular_buffer *cb2);

typedef enum {
  RAW_ENERGY=0,
  NORM_ENERGY,
  MIN_NORM_ENERGY,
  MAX_NORM_ENERGY,
  KURTOSIS,
  MEAN_XCOR,
  MAX_XCOR
} FeatType ;

const int NFEATS=7; 
const real PI=4*atan(1);

fftwf_complex *fft_in;
fftwf_complex *fft_out;
fftwf_plan fft;
fftwf_plan ifft;
real **fft_mem;
real *hamming;
Allocator *allocator;

void ParseCmdLine(CmdLine *cmd, int argc, char *argv[]);

char *save_dir;
char *save_ext;

int main(int argc, char **argv) {

  //---------------------------------------------------------------------------
  //
  // process the command line arguments
  //
  //---------------------------------------------------------------------------

  allocator = new Allocator;

  feat_f = (bool*)allocator->alloc(sizeof(bool)*NFEATS);

  //=================== The command-line ==========================

  // Construct the command line
  CmdLine cmd;

  ParseCmdLine(&cmd,argc,argv);

  // setup hamming window if needed!
  if (window_f){
    hamming = (real*)allocator->alloc(sizeof(real)*frame_size);
    for (int i = 0; i < frame_size; i++){
      hamming[i] = 0.54 - 0.46*cos(2*PI*i/(frame_size-1));
    }
  }

  // setup FFT plan
  fft_in = (fftwf_complex*) fftwf_malloc(sizeof(fftwf_complex) * frame_size);
  fft_out = (fftwf_complex*) fftwf_malloc(sizeof(fftwf_complex) * frame_size);
  fft = fftwf_plan_dft_1d(frame_size, fft_in, fft_out, FFTW_FORWARD, FFTW_MEASURE);
  ifft = fftwf_plan_dft_1d(frame_size, fft_out, fft_in, FFTW_BACKWARD, FFTW_MEASURE);
  fft_mem = (real**)allocator->alloc(sizeof(real*)*frame_size);
  *fft_mem = (real*)allocator->alloc(sizeof(real)*frame_size*2);
  for (int i = 1; i < frame_size; i++){
    fft_mem[i] = *fft_mem+i*2;
  }

  int NCHAN = ref_files.nargs;
  FILE **fp_ref  = NULL;
  fp_ref = (FILE **)allocator->alloc(sizeof(FILE*)*NCHAN);
  for (int i = 0; i < NCHAN; i++){
    if (!(fp_ref[i] =  fopen(ref_files.args[i],"rb"))){
      error("Can not open reference file: %s");
    }
    fseek(fp_ref[i],skip,SEEK_SET);
  }

  // first pass simply determine the number of frames that we need..
  unsigned long NFRAMES=ULONG_MAX;
  for (int i = 0; i < NCHAN; i++){
    unsigned long nfr = 0;
    struct stat buf;
    int hnd = fileno(fp_ref[i]);
    fstat(hnd,&buf);
    unsigned long flength =  buf.st_size/sizeof(short);
    nfr = (unsigned long)((flength-frame_size-skip)/frame_shift + 1);

    if (nfr < NFRAMES){
      NFRAMES = nfr;
    }
  }

  message("%i frames detected",NFRAMES);
  
  // now for the HTK header and file output... 
  IOHTKHeader htk_head;
  htk_head.n_samples = NFRAMES;  //endianSwap(&(htk_head.n_samples), sizeof(long));
  htk_head.sample_period = (long)((real)frame_shift * 1E7 / sample_frequency); //endianSwap(&(htk_head.sample_period), sizeof(long));
  htk_head.sample_size = 0;
  for (int k = 0; k < NFEATS; k++){
    htk_head.sample_size += feat_f[k]*sizeof(float);
  }
  //endianSwap(&(htk_head.sample_size),sizeof(short));
  htk_head.sample_kind = (compress_f ? FEAT_USER | _C : FEAT_USER); //endianSwap(&(htk_head.sample_kind),sizeof(short));

  float ***feats = (float***)allocator->alloc(sizeof(float**)*NCHAN);
  for (int i = 0; i < NCHAN; i++){
    feats[i] = (float**)allocator->alloc(sizeof(float*)*NFEATS);
    for (int j = 0; j < NFEATS; j++){
      //if (feat_f[j] || j == RAW_ENERGY) // one always needs some raw energy!
      feats[i][j] = (float*)allocator->alloc(sizeof(float)*NFRAMES);
    }
  }

  // allocate some storage space for xcor... 
  real **xcor = NULL;
  if (feat_f[MEAN_XCOR] || feat_f[MAX_XCOR]){
    xcor = (real**)allocator->alloc(sizeof(real*)*NCHAN);
    for (int i = 0; i < NCHAN; i++){
      xcor[i] = (real*)allocator->alloc(sizeof(real)*NCHAN);
    }
  }

  // now for the file analysis...
  short sig;//, prev_sig = 0;
  Circular_buffer **cb = (Circular_buffer**) allocator->alloc(sizeof(Circular_buffer*)*NCHAN);
  for (int i = 0; i < NCHAN; i++){
    cb[i] = new(allocator) Circular_buffer();
    cb[i]->allocate_cc(frame_size);
  }
  short *prev_sig = (short*)allocator->alloc(sizeof(short)*NCHAN);

  for (int i = 0; i < NCHAN; i++){
    prev_sig[i] = 0;
    //prev_sig = 0;
    for (int t = 0; t < frame_size - frame_shift; t++){
      fread(&sig,sizeof(short),1,fp_ref[i]);
      if (hpfilter_f){
	*(cb[i]) = 0.9903*sig - 0.9903*prev_sig[i] + .9806*(*cb[i])(0);
	//*(cb[i]) = 0.9903*sig - 0.9903*prev_sig + .9806*(*cb[i])(0);
	//prev_sig = sig;
	prev_sig[i] = sig;
      }else{
	*(cb[i]) = sig;
      }
    }
  }

  for (unsigned int j = 0; j < NFRAMES; j++){
    for (int i = 0; i < NCHAN; i++){
      for (int t = 0; t < frame_shift; t++){
	fread(&sig,sizeof(short),1,fp_ref[i]);
	if (hpfilter_f){
	  *(cb[i]) = 0.9903*sig - 0.9903*prev_sig[i] + .9806*(*cb[i])(0);
	  //*(cb[i]) = 0.9903*sig - 0.9903*prev_sig + .9806*(*cb[i])(0);
	  //prev_sig = sig;
	  prev_sig[i] = sig;
	}else{
	  *(cb[i]) = sig;
	}
      }
    }
    for (int i = 0; i < NCHAN; i++){
      if (feat_f[RAW_ENERGY] || feat_f[NORM_ENERGY] || feat_f[MAX_XCOR] ||  feat_f[MIN_NORM_ENERGY] ){ //  energy feature (also used in other calculations
	feats[i][RAW_ENERGY][j] = (float)calc_energy(cb[i]);
      }

      if (feat_f[KURTOSIS]){  // kurtosis
	feats[i][KURTOSIS][j] = (float)calc_kurtosis(cb[i]);
      }

      if (feat_f[MEAN_XCOR] || feat_f[MAX_XCOR]){   //  some cross correlation measures
	for (int k = i; k < NCHAN; k++){
	  if (i != k){ // no need for auto correlation
	    xcor[i][k] = calc_max_xcor(cb[i],cb[k]);
	    xcor[k][i] = xcor[i][k];
	  }
	}
	if (feat_f[MEAN_XCOR]){
	  feats[i][MEAN_XCOR][j] = 0.0;
	  for (int k = 0; k < NCHAN; k++){
	    if (k != i)
	      feats[i][MEAN_XCOR][j] += xcor[i][k];
	  }
	  feats[i][MEAN_XCOR][j] /= NCHAN - 1;
	}
	if (feat_f[MAX_XCOR]){
	  feats[i][MAX_XCOR][j] = 0.0;
	  for (int k = 0; k < NCHAN; k++){
	    if (i != k)
	      if (xcor[i][k] > feats[i][MAX_XCOR][j] && k != i){
		feats[i][MAX_XCOR][j] = xcor[i][k]; 
	      }
	  }
	  feats[i][MAX_XCOR][j] /= feats[i][RAW_ENERGY][j];
	}
      }
    }    
  }

  //real *energy_floor = (real*)allocator->alloc(sizeof(real)*NCHAN );  // energy floor does not seem to be a good idea
  //for (int i = 0; i < NCHAN; i++){
  //  energy_floor[i] = FLT_MAX;
  //  for (unsigned int j = 0; j < NFRAMES; j++){
  //    if (feats[i][RAW_ENERGY][j] < energy_floor[i])  
  //	energy_floor[i] = feats[i][RAW_ENERGY][j];
  //  }
  //}

  // cross channel normalised energy measure
  for (unsigned int j = 0; j < NFRAMES; j++){
    // noise flooring does not seem to be effective
    //for (int i = 0; i < NCHAN; i++){
    //  feats[i][RAW_ENERGY][j] = logSub(feats[i][RAW_ENERGY][j],energy_floor[i]); //exp(feats[i][RAW_ENERGY][j]) - exp(energy_floor[i]);
    //  feats[i][RAW_ENERGY][j] = feats[i][RAW_ENERGY][j] < -50 ? -50 : feats[i][RAW_ENERGY][j]; // noise floor of -50
    //}
    if (feat_f[NORM_ENERGY]){
      real mix_e = feats[0][RAW_ENERGY][j];
      for (int k = 1; k < NCHAN; k++){
      	mix_e = logAdd(mix_e,feats[k][RAW_ENERGY][j]);  //mix_e+feats[k][RAW_ENERGY][j];
      }

      for (int i = 0; i < NCHAN; i++){
	/////////////////////////////////////////////////////////////////////////////
	//  some alternative normalised energy measures were tried without success //
	/////////////////////////////////////////////////////////////////////////////

	//real max_e = FLT_MIN; 
	//for (int k = 0; k < NCHAN; k++){
	//  if (feats[k][RAW_ENERGY][j] > max_e && k != i){
	//    max_e = feats[k][RAW_ENERGY][j];
	//  }
	//}

	//real mix_e = 0;
	//for (int k = 0; k < NCHAN; k++){
	//  if (k != i)
	//    mix_e = logAdd(mix_e,feats[k][RAW_ENERGY][j]);
	//}
	//mix_e /= NCHAN-1;

	feats[i][NORM_ENERGY][j] = feats[i][RAW_ENERGY][j] - mix_e;
      }
    }

    if (feat_f[MIN_NORM_ENERGY]){
      for (int k = 0; k < NCHAN; k++){
      real min_e = FLT_MAX;
      real max_e = -FLT_MAX;
	for (int i = 0; i < NCHAN; i++){
	  if (k != i){
	    if (feats[i][RAW_ENERGY][j] < min_e){
	      min_e = feats[i][RAW_ENERGY][j];
	    }
	    if (feats[i][RAW_ENERGY][j] > max_e){
	      max_e = feats[i][RAW_ENERGY][j];
	    }
	  }
	}
	feats[k][MIN_NORM_ENERGY][j] = feats[k][RAW_ENERGY][j] - min_e;
	feats[k][MAX_NORM_ENERGY][j] = feats[k][RAW_ENERGY][j] - max_e;
      }
    }
  }

  Sequence *seq = new(allocator) Sequence(NFRAMES,  htk_head.sample_size/sizeof(float));

  // now write the features out to a file
  for (int i = 0; i < NCHAN; i++){
    DiskXFile *fp_out;
    char *outfile1 =  strRemoveSuffix(ref_files.args[i]);
    char *outfile2 = strBaseName(outfile1);
    char *outfile3 = strConcat(5,save_dir,"/",outfile2,".",save_ext);
    fp_out = new(allocator) DiskXFile(outfile3,"wb+");

    //fwrite(&htk_head,sizeof(IOHTKHeader),1,fp_out);
    message("  Channel %i,  %s", i, outfile3);
    free(outfile1);
    free(outfile3);
    
    for (unsigned int j = 0; j < NFRAMES; j++){
      for (int k = 0, m = 0; k < NFEATS; k++){
    	if (feat_f[k]){
	  seq->frames[j][m++] = feats[i][k][j];
    	}
      }
    }

    IOHTKFeat::saveSequence(fp_out, seq, &htk_head);

    //for (unsigned int j = 0; j < NFRAMES; j++){
    //  for (int k = 0; k < NFEATS; k++){
    //	if (feat_f[k]){
    //	  endianSwap(&(feats[i][k][j]), sizeof(float));
    //	  fwrite(&(feats[i][k][j]),sizeof(float),1,fp_out);
    //	}
    //  }
    //}
    allocator->free(fp_out);
  }

  delete allocator;

  message("==================");

  fftwf_destroy_plan(fft);
  fftwf_destroy_plan(ifft);
  fftwf_free(fft_in);
  fftwf_free(fft_out);

  // exit gracefully
  //
  return(0);
}

void ParseCmdLine(CmdLine *cmd, int argc, char *argv[]){
  // Put the help line at the beginning
  cmd->info(help);

  ref_files.isArgument(true);

  cmd->addText(                                               "\nArguments:                                   ");
  cmd->addCmdOption(&ref_files);

  cmd->addText(                                                       "\nFeature Options:                             ");
  cmd->addBCmdOption("-norm_energy", &(feat_f[NORM_ENERGY]),false,      "normalised energy                            ");
  cmd->addBCmdOption("-raw_energy", &(feat_f[RAW_ENERGY]),false,        "raw energy                                   ");
  cmd->addBCmdOption("-min_max_energy", &(feat_f[MIN_NORM_ENERGY]),false, "energy normaed by min & max of other chans   ");  cmd->addBCmdOption("-kurtosis",   &(feat_f[KURTOSIS]),false,          "signal kurtosis                              ");
  cmd->addBCmdOption("-mean_xcor",  &(feat_f[MEAN_XCOR]),false,           "mean cross-correlation across channels       ");
  cmd->addBCmdOption("-max_norm_xcor",   &(feat_f[MAX_XCOR]),false,           "max normalised correlation across channels   ");

  cmd->addText(                                               "\nPreprocessing Options:                       ");
  cmd->addICmdOption("-sample_frequency", &sample_frequency,16000,            "sample frequency (Hz)                        ");
  cmd->addICmdOption("-frame_size", &frame_size,400,            "frame size (samples)                         ");
  cmd->addICmdOption("-frame_shift",&frame_shift,160,           "frame shift (samples)                        ");
  cmd->addBCmdOption("-frame_window",&window_f,false,           "hamming windowing                            ");
  cmd->addBCmdOption("-hp_filter",&hpfilter_f,false,            "high pass filtering of signal                ");
  cmd->addICmdOption("-skip", &skip, 0,                         "Skip N bytes at beginning of raw file        ");

  cmd->addText(                                               "\nOutput Options:                       ");
  cmd->addSCmdOption("-output_dir", &save_dir,".",              "save to the following directory              ");
  cmd->addSCmdOption("-output_ext", &save_ext,"ft",             "save with the following extension            ");
  cmd->addBCmdOption("-compress",   &compress_f,false,          "save in compressed HTK format                ");

  // Read the command line
  cmd->read(argc, argv);

  //if (norm_energy_f + raw_energy_f + zcr_f + kurtosis_f + freqkur_f + voicing_f == 0){
  //  error("You must select ar least one feature extraction flag... ");
  // }

  printf("# Generating:  ");
  if (feat_f[NORM_ENERGY])
    printf("norm_energy ");
  if (feat_f[RAW_ENERGY])
    printf("raw_energy ");
  if (feat_f[MIN_NORM_ENERGY]){
    feat_f[MAX_NORM_ENERGY] = true;
    printf("min_max_energy ");
  }else{
    feat_f[MAX_NORM_ENERGY]=false;
  }
  if (feat_f[KURTOSIS])
    printf("signal_kurtosis ");
  if (feat_f[MEAN_XCOR])
    printf("mean_xcor ");
  if (feat_f[MAX_XCOR])
    printf("max_norm_xcor ");

  if (window_f || hpfilter_f){
    printf("[ ");
    if (window_f)
      printf("hamming_window ");
    if (hpfilter_f)
      printf("high_pass_filter ");
    printf("]");
  }
  printf("\n"); 

  message("  sample_frequency (%i) frame_size (%i) frame_shift (%i)",sample_frequency,frame_size,frame_shift);
  message("");
 
}


real calc_max_xcor(Circular_buffer *cb1, Circular_buffer *cb2){
  real max_xcor = 0;

  if (window_f){
    for (int i = 0; i < frame_size; i++){
      fft_in[i][0] = (*cb1)(-i)*hamming[i];
      fft_in[i][1] = 0;
    }
  }else{
    for (int i = 0; i < frame_size; i++){
      fft_in[i][0] = (*cb1)(-i);
      fft_in[i][1] = 0;
    }
  }

  // fft of the first frame
  fftwf_execute(fft);

  for (int i = 0; i < frame_size; i++){
    fft_mem[i][0] = fft_out[i][0];
    fft_mem[i][1] = fft_out[i][1];
  }

  if (window_f){
    for (int i = 0; i < frame_size; i++){
      fft_in[i][0] = (*cb2)(-i)*hamming[i];
      fft_in[i][1] = 0;
    }
  }else{
    for (int i = 0; i < frame_size; i++){
      fft_in[i][0] = (*cb2)(-i);
      fft_in[i][1] = 0;
    }
  }

  // fft of the second frame
  fftwf_execute(fft);

  real R, I;
  for (int i = 0; i < frame_size; i++){
    R = fft_out[i][0]*fft_mem[i][0] + fft_out[i][1]*fft_mem[i][1];
    I = -fft_out[i][0]*fft_mem[i][1] - fft_out[i][1]*fft_mem[i][0];

    fft_out[i][0] = R;
    fft_out[i][1] = I;
  }

  fftwf_execute(ifft);

  // look for the maximum xcor, we only keep the real part here 
  // (numerical rounding will cause a small imaginary part to be present)
  for (int i = 0; i < frame_shift; i++){ 
    if (fft_in[i][0] > max_xcor){
      max_xcor = fft_in[i][0];
    }
  }
  max_xcor /= frame_size;  // as we are using an unormalised fft

  return max_xcor;
}

real calc_energy(Circular_buffer *cb){
  real ans=0.0;

  if (window_f){
    for (int i = 0; i < frame_size; i++){
      ans += (*cb)(-i)*(*cb)(-i)*hamming[i]*hamming[i];
    }
  }else{
    for (int i = 0; i < frame_size; i++){
      ans += (*cb)(-i)*(*cb)(-i);
    }
  }

  ans = log(sqrt(ans)+0.0001);

  return ans;
}

// 
real calc_kurtosis(Circular_buffer *cb){
  real ans=0.0;
  real m1 = 0.0;
  real m2 = 0.0;
  real m4 = 0.0;   
  if (window_f){
    for (int i = 0; i < frame_size; i++){
      m1 += (*cb)(-i)*hamming[i];
    }
    m1 /= frame_size;

    for (int i = 0; i < frame_size; i++){
      m2 += ((*cb)(-i)*hamming[i] - m1)*((*cb)(-i)*hamming[i] - m1);
      m4 += m2*m2;
    }
  }else{
    for (int i = 0; i < frame_size; i++){
      m1 += (*cb)(-i);
    }
    m1 /= frame_size;
    
    for (int i = 0; i < frame_size; i++){
      m2 += ((*cb)(-i) - m1)*((*cb)(-i) - m1);
      m4 += m2*m2;
    }
  }
  m2 /= frame_size;
  m4 /= frame_size;

  ans = (m4+FLT_MIN)/(m2*m2+FLT_MIN);
  
  return ans;
}


