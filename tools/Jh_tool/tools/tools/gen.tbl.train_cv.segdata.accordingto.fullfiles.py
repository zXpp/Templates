#!/usr/bin/python
# This script is to generate a new segment MLF files by merging detail labs in the old MLF file
#
import os,sys
path = '/share/spandh.ami1/usr/yanxiong/data/tbl/manual.ref'
filename = 'tbl.train.mlf'
f1 = path + '/%s' % filename
f2 = path + '/%s.seg' % filename

mlf1 = open(f1,'r')
line1 = mlf1.readline() # read the first line
mlf2 = open(f2,'wa')
mlf2.write(line1) # write the first line

while True:
    line1 = mlf1.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
        fn = line1[0:16]  # extract file name
    elif 'SPEECH' in line1:
        line2 = line1.split()
        x1 = int(line2[0]) / 100000 # start point
        x2 = int(line2[1]) / 100000 # end point
        xx1 = str(x1)
        xx2 = str(x2)
        while True:
            if len(xx1) < 6:
                xx1 = '0' + xx1
            else:
                break
        while True:
            if len(xx2) < 6:
                xx2 = '0' + xx2
            else:
                break
        segname = fn + '_' + xx1 + '_' + xx2 + '.lab"\n'
        mlf2.write(segname) # write segment name
        
        endpoint = str(x2 - x1 + 1)
        mlf2.write('0 ') # write start point
        mlf2.write(endpoint + '00000 ') # write end point
        mlf2.write(line2[2]) # write label name
        mlf2.write('\n.\n')

mlf1.close
mlf2.close            
