#!/usr/bin/python
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/auxfea_fbank/auxfea_fbank.filename','r')
f2 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/auxfea_fbank/auxfea_fbank.filepath','w')
path1 = '/share/spandh.ami1/usr/yanxiong/data/rt07/fbank/complete/'
path2 = '/share/spandh.ami1/usr/yanxiong/data/rt07/auxfea_combined/'
suffix2 = '.auxcom'
while True:
    line1 = f1.readline() # read one line
    if not line1:
        break
    line2 = line1.split()
    f2.write(path1)
    f2.write(line2[0])    # write one line
    f2.write(' ')
    f2.write(path2)
    f2.write(line2[0][:20])    # write one line
    f2.write(suffix2)
    f2.write('\n')
f1.close
f2.close

