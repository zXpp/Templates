#!/bin/bash
scp_file="/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/train_hcopy_tmp.scp"
config_file="/home/zzpp220/HTK/mob2mfcc.cfg"
sample_num=`wc -l $scp_file|gawk '{print $1}'`

start=`date +%s.%N`
HCopy -A -D -C "$config_file" -S "$scp_file"
stop=`date +%s.%N`
echo $start;echo $stop
echo " use total time: `echo "scale=3;$stop-$start"|bc`s
