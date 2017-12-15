#!/usr/bin/python
# # This script is to generate scp lines according to one MLF file
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/ExtrAuxFea/rt07_aux.list','r')
#f2 = open('/share/spandh.ami1/usr/yanxiong/data/ami/fbank/complete/ami_fbank','r')
f2 = open('/share/spandh.ami1/usr/yanxiong/ExtrAuxFea/combined_rt07_aux.list','w')
iter = 0
line1 = f1.readline() # read one line
line2 = line1.split()
f2.write(line2[0])    # write one line
f2.write(' ')
len = 20
lastfile = line2[0][:len]
while True:
    line1 = f1.readline() # read one line
    if not line1:
        break
    line2 = line1.split()
    if line2[0][:len] == lastfile:
        f2.write(line2[0])    # write one line
        f2.write(' ')
    else:
        f2.write('\n')
        f2.write(line2[0])    # write one line
        f2.write(' ')
        lastfile = line2[0][:len]
f1.close
f2.close

