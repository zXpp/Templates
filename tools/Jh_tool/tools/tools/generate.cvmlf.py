#!/usr/bin/python
# This script is to generate a new segment MLF files by merging detail labs in the old MLF file
#
import os,sys
mlf1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.sad.fbank/ami.mlf','r')
line1 = mlf1.readline() # read the first line
mlf2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.sad.fbank/cv.mlf','wa')
mlf2.write(line1) # write the first line
iter = 0   #  iteration number
while True:
    line1 = mlf1.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
        iter = iter + 1
        if iter % 10 == 0:
            mlf2.write(line1)  # write the first line
            line1 = mlf1.readline() 
            mlf2.write(line1)        # write the second line
            line1 = mlf1.readline()
            mlf2.write(line1) # write the third line  
mlf1.close
mlf2.close            
