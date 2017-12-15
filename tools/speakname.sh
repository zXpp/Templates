#!/bin/bash
#set -x
#set -e
#for file in ~/Documents/score/sys_tmp/*.sys.rttm
for file in {"apple.chain","banna.chain"}
do
	#tmpname=basename $file .sys.rttm
	tmpname=$(basename $file .chain)
	#sed "s/chain/($tmpname)/g" $file
	echo $file
done
