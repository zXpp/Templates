#!/bin/bash

#this script is to addnoise on pure wav under $wavpath,and then use hcopy to extract mfcc from noise-added wav-files,
#

wavpath=/media/zzpp220/Data/Linux_Documents/Mobile/zx_mobile_test/sample_test/040-079/WAV_ZX_MOBILE
label=babble1
noisewav=/media/zzpp220/Data/Linux_Documents/Mobile/zx_mobile_test/noise/${label}16.wav
rawnoisewav=/media/zzpp220/Data/Linux_Documents/Mobile/DATA/Noise_NOISEX-92/${label}.wav
snr=[-30,-20,-10,-5]

MATLAB="/usr/local/MATLAB/R2015b/bin/matlab -nojvm -nosplash -r "
mfilepath=/home/zzpp220/Templates/tools/mianmean120_function_sendto_kmeans+accur
wavroot=`dirname $wavpath`/${label} #wav's pardir or otherdir  at same level of ,matlab will make it
echo wavroot: $wavroot
morder="addpath(genpath('$mfilepath'));multi_zx_utf8addnoisemono('$wavpath','$noisewav','$label',$snr,'$wavroot'); 'exit';"
echo "matlab order " $morder
if [ -e "${noisewav}" ];then
		echo `basename ${noisewav}` already exist
else
	#echo touch ${res_file}
	sox $rawnoisewav -b 16 -r 16000 $noisewav
fi

$MATLAB "addpath(genpath('$mfilepath'));multi_zx_utf8addnoisemono('$wavpath','$noisewav','$label',$snr,'$wavroot'); exit;" ;
#'' is to change the str(under shell) into str(under) matlab
for x in $wavroot/WAV_${label}*dB
do

	mfccdir=${wavroot}/MFCC13_`basename $x`
	if [ -d "${mfccdir}" ];then
		echo $mfccdir already exists
	else
		echo "making $mfccdir"
		mkdir $mfccdir
	fi
	echo $x #abs dir tot
	python2 ~/Templates/tools/Jh_tool/jh_hcopy_scp.py $x $mfccdir mfcc ${label}`basename $x`
done

for y in $wavroot/*.scp
do
	echo extracting mfccfile in $y
	~/HTK/HCopy -A -C ~/HTK/mob2mfcc.cfg -S $y;echo `basename $x` extracted sucessfully
done