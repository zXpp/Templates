#!/bin/sh

#/***************************************************************************
# *   copyright            : (C) 2011 by Karel Vesely,UPGM,FIT,VUT,Brno     *
# *   email                : iveselyk@fit.vutbr.cz                          *
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the APACHE License as published by the          *
# *   Apache Software Foundation; either version 2.0 of the License,        *
# *   or (at your option) any later version.                                *
# *                                                                         *
# ***************************************************************************/

# generates gmmbypass to use with HTK decoder on posterior features

if [ $# != 2 ]; then 
  echo "$0 dict(i) hmmdefs_file(o)"; exit 1;
fi

dict=$1
hmmdefs_file=$2

C=1.0

##########################################################
#make hmmdefs

#number of phonemes
num_phn=`wc $dict | awk '{print $1}'`

zero=""
for((i=0;$i<$num_phn;i++));do
  zero="$zero 0"
done


echo " ~o <VecSize> $num_phn <USER> " > $hmmdefs_file

count=0;
for phn in `cat $dict`; do
  tmp=""
  for((i=0;$i<$num_phn;i++));do
    if [ $i -eq $count ]; then
      tmp="$tmp $C"
    else
      tmp="$tmp 1e30"
    fi
  done
  count=$((count + 1))

    echo "~s \"$phn\"
    <Mean> $num_phn
      $zero
    <Variance> $num_phn
      $tmp 
    <GConst> 0">> $hmmdefs_file

done


for phn in `cat $dict | sed 's/\(.*\)__[0-9]/\1/'|sort|uniq`; do
echo "~h \"$phn\"
 <BeginHMM>
   <NumStates> 5
   <State> 2 ~s \"${phn}\"
   <State> 3 ~s \"${phn}\"
   <State> 4 ~s \"${phn}\"
   <TransP> 5
      0  1   0   0   0
      0  0.5 0.5 0   0
      0  0   0.5 0.5 0
      0  0   0   0.5 0.5
      0  0   0   0   0
   <EndHMM>" >> $hmmdefs_file
done


