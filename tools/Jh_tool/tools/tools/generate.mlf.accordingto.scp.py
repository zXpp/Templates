#!/usr/bin/python
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.meetings/cv.fbank.scp','r')
f2 = open('/share/spandh.ami1/usr/yanxiong/tnet.meetings/cv.mlf','wa')
f2.write('#!MLF!#\n')
while True:
    line1 = f1.readline()
    if not line1:
        break
    if 'applause' in line1:
        temp1 = line1[0:13]
        str1 = 'APPLAUSE'
    if 'laughter' in line1:
        temp1 = line1[0:13]
        str1 = 'LAUGHTER'
    if 'silence' in line1:
        temp1 = line1[0:12]
        str1 = 'SILENCE'
    if 'speech' in line1:
        temp1 = line1[0:11]
        str1 = 'SPEECH'
    temp2 = '"*/' + temp1 + '.lab"'
    f2.write(temp2)
    f2.write('\n')
    f2.write('0 0 ')
    f2.write(str1)
    f2.write('\n')
    f2.write('.\n')
f1.close
f2.close            
