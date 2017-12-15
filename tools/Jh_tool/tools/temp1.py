#!/usr/bin/python
# This script is to generate a new segment MLF files by merging detail labs in the old MLF file
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/data/meetings/fbank/laughter.wav2fbank.scp','r')
f2 = open('/share/spandh.ami1/usr/yanxiong/data/meetings/fbank/laughter.wav2fbank.scp.new','wa')
num = int(1)
while True:
    line1 = f1.readline()
    if not line1:
        break
    line2 = line1.split()
    if num < 10:
        str1 = '00' + str(num)
    if num >=10 and num < 100:
        str1 = '0' + str(num)
    if num >=100 and num < 1000:
        str1 = str(num)

    temp1 = line2[0] + str1 + '.wav'
    temp2 = line2[1] + str1 + '.fbk'
    f2.write(temp1)
    f2.write(' ')
    f2.write(temp2)
    f2.write('\n')
    num = num + 1
f1.close
f2.close
