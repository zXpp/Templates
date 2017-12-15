#!/bin/bash
#this is for handle scp 
for file in /home/zzpp220/Documents/mobile/DATA/chain/*/t*/*.scp
do
	python /home/zzpp220/Templates/tools/SCP2ILPSEG.py $file
	 
done
mv -f `pwd`/*.m.seg /home/zzpp220/Documents/ILP_RAR/LIUM-master/test_out/
mv -f `pwd`/*.n.seg /home/zzpp220/Documents/ILP_RAR/LIUM-master/test_out/
