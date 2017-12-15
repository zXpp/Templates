#!/bin/bash
for file in ~/Documents/mobile/DATA/chain/*/t*/*.txt
do
	dirna=`dirname $file`
    echo $dirna 	
    tmpname=grep ".TextGrid" $dirna/*
   echo  $tmpname
    basname=`basename $tmpname .TextGrid`
    echo $basname 
	#mv $file $file
done
