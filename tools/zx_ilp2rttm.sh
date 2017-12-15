#!/bin/bash
# this script is to change the ilp format file to rttm format ,if reuse,just change the dir path at line 3 and suffix at line 9
dir=$2
ilpfile_dir=/home/zzpp220/Documents/score/$dir
thr=$1
for file in $ilpfile_dir/*.ev_is.$thr.seg
do 
  if [ -f "$file" ]
  then 
       cat $file |grep -v ';' |sort -k 3 -n >tmp.txt
       newname=`basename $file .ev_is.$thr.seg`.sys.rttm
       gawk '{printf " SPEAKER  %-s 1  %-7.3f  %-7.3f    <NA>  <NA>  %4s    <NA>\n",$1,$3/100,$4/100,$8}' tmp.txt > $ilpfile_dir/$newname
       rm tmp.txt
  fi
done
