#!/bin/bash
# This script is to delete the fourth column and delete spaces at the start and end of one row
# 

awk '{$4="";print}' wka.sad.mlf > test1.mlf && mv test1.mlf wka.sad.mlf # delete the fourth column

sed  's/^[ \t]*//g' wka.sad.mlf > test1.mlf && mv test1.mlf wka.sad.mlf

sed 's/[ \t]*$//g' wka.sad.mlf > test1.mlf && mv test1.mlf wka.sad.mlf
