#!/bin/bash
rootdir=/home/zzpp220/Documents/LIUM-master
textgridfile_dir=/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TEST/zx_Mobile/textGrid
#rttmfile_dir=$rootdir/newchain_praat2rttm
rttmfile_dir=/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TEST/zx_Mobile
mode='test'
for file in $textgridfile_dir/*.textGrid
do  
  if [ -f "$file" ]
  then
	#echo $file
	   python2.7 ~/Templates/tools/textgrid2rttm.py $file $mode
	   echo ok    
  fi
done
mv `pwd`/*.ref.rttm $rttmfile_dir/
