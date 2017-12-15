#!/bin/bash
## this script is to change the feature file in htk format into gz format
MATLAB="/home/zzpp220/Matlab/bin/matlab -nojvm -nosplash"

 #change the feature of htk format to text format
 #do
  #../bin/aibfeat --config $CFG_FILE --mfcc ../data/mfcc/$id.fea 1.0 --scp ../data/$id.scp --id $id
filedir="/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/train/direct_mfcc51/" #path must be full with the last #"/" 
#destdir="/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/test/mfcc_17/"
destdir=$filedir
header="train_chain"
suffix=".fea"
suffix1=fea
script=/home/zzpp220/Documents/LIUM-master/chain_htk_mfcc/htk2cmu_gz.m
$MATLAB -r "htk2cmu_gz('$header','$filedir','$destdir','$suffix'); exit;" ;

###gzip the text files
for text_file in $destdir/*.$suffix1
do
	gzip $text_file
done
