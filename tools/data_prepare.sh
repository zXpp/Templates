#!/bin/bash
set -e
#set -x
:<<BLOCK
a=12
b=19
`seq $a $b`
eval echo {$a..$b}
BLOCK
rootdir=/media/zzpp220/Data/Linux_Documents/Mobile/zx_mobile_test/sample_test
wavset_dir=/media/zzpp220/Entertaminment/zx/MobileData_Zx
fea=MFCC13
cd $rootdir
for x in 560-599
do
	fir=`echo $x|cut -d "-" -f 1`
	sec=`echo $x|cut -d "-" -f 2`
	echo $fir, $sec
	if [ -d $x ];then
		echo "$x already exist"
	else
		echo "mkdir $x"
	fi
	mkdir -p $x/{WAV,$x-$fea,$x-GMM13,res}
	range=`seq $fir $sec`
	#for y in $range
	#do
	#	cp -a ${wavset_dir}/*/Eng/*/*_$y.wav $x/WAV
	#done
	
	echo "\nWAV NUM:`ls -l $x/WAV|grep "^-"|wc -l`"
	hcopyfile=$x-hcopy.scp
	python2 ~/Templates/tools/Jh_tool/jh_hcopy_scp.py `pwd`/$x/WAV `pwd`/$x/$x-$fea mfcc $x-hcopy
	echo "\nEXTRACTING FEATURE ......."
	#mv $hcopyfile $
	HCopy -A -C ~/HTK/mob2mfcc.cfg -S $hcopyfile
	echo "\nEXTRACT FEATURE ..OK"
	echo "\n$fea NUM:`ls -l $x/$x-$fea|grep "^-"|wc -l`"
	#echo `basename $x`
	7zr a $x-$fea.7z `pwd`/$x/$x-$fea
done
 
