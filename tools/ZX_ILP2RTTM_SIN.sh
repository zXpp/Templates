#!/bin/bash
#usage:eg:source ~/Templates/tools/ZX_ILP2RTTM_SIN.sh ./$datadir/$show.ev_is.$c.seg $c ./$datadir
file=$1
thr=$2
destdir=$3
cat $file |grep -v ';' |sort -k 3 -n >tmp.txt
       newname=`basename $file ".ev_is.$thr.seg"`.sys.rttm
       gawk '{printf " SPEAKER  %-s 1  %-7.3f  %-7.3f    <NA>  <NA>  %4s    <NA>\n",$1,$3/100,$4/100,$8}' tmp.txt > $newname
       rm tmp.txt
       mv $newname $destdir/
