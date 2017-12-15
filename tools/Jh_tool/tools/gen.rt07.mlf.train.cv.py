#!/usr/bin/python
# This script is to generate MLF file of training or CV data for rt07
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-rt07.sad/rt07_partlytrain/onlyfbank/train.mlf.original','r')
line1 = f1.readline() # read the first line
f2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-rt07.sad/rt07_partlytrain/onlyfbank/train.mlf','wa')
f2.write(line1) # write the first line
while True:
    line1 = f1.readline()
    if not line1:
        break
    if 'lab' in line1:
        prefix = line1[:23]  #extract the prefix of file name
    elif 'SPEECH' in line1:
        line2 = line1.split()
        tmp1 = str(int(line2[0])/100000)
        while len(tmp1) < 6:
            tmp1 = '0' + tmp1
        tmp2 = str(int(line2[1])/100000)
        while len(tmp2) < 6:
            tmp2 = '0' + tmp2
        filename = prefix + '_' + tmp1 + '_' + tmp2 + '.lab"\n'
        f2.write(filename)
        f2.write('0')
        f2.write(' ')
        diff = str((int(line2[1])/100000 - int(line2[0])/100000)*100000 + 100000)
        f2.write(diff)
        f2.write(' ')
        f2.write(line2[2])
        f2.write('\n') 
        f2.write('.\n')
f1.close
f2.close
