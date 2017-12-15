#!/usr/bin/python
# This script is to transform phonems list in one MLF into SPEECH/NONSPEECH list and then
# write these SPEECH/NONSPEECH into another MLF file
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.meetings/cv.mlf','r')
f2 = open('/share/spandh.ami1/usr/yanxiong/tnet.meetings/cv.mlf.new','wa')
f2.write('#!MLF!#\n')
while True:
    line1 = f1.readline()
    if not line1:
        break
    line2 = line1.split()
    if 'lab' in line1:
        f2.write(line1)
        if 'applause' in line1:
            temp1 =  line2[0][3:16]
        if 'laughter' in line1:
            temp1 =  line2[0][3:16]
        if 'silence' in line1:
            temp1 =  line2[0][3:15]
        if 'speech' in line1:
            temp1 =  line2[0][3:14]     
        print temp1
        f3 = open('/share/spandh.ami1/usr/yanxiong/data/meetings/lines.txt', 'r')
        while True:
            line1 = f3.readline()
            if not line1:
                break
            if temp1 in line1:
                line2 = line1.split()
                endpoint = line2[1] + '00000'
                break
        f3.close           
        line1 = f1.readline()
        line2 = line1.split()        
        f2.write('0 ')
        f2.write(endpoint)
        f2.write(' ')
        f2.write(line2[2])
        f2.write('\n')
        f2.write('.\n')
f1.close
f2.close            
