#!/bin/bash
#exec 0</home/zzpp220/Documents/mobile/DATA/mix-data/text/chain.scp

scpdir=$1
for file in $scpdir/*.scp
do  
  if [ -f "$file" ]
  then
	#echo $file
	   python2.7 ~/Templates/tools/SCP2ILPSEG.py $file    
  fi
done
