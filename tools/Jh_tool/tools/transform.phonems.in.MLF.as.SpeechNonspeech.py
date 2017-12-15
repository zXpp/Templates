#!/usr/bin/python
# This script is to transform phonems list in one MLF into SPEECH/NONSPEECH list and then
# write these SPEECH/NONSPEECH into another MLF file
#
import os,sys
f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/ami.phonems.mlf','r')
line1 = f1.readline()
f2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/ami.SpeechNonspeech.mlf','wa')
f2.write(line1)
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif '.lab' in line1:
        f2.write(line1)
    elif ' sil' in line1:
        line2 = line1.split()
        f2.write(line2[0])
        f2.write(' ')
        f2.write(line2[1])
        f2.write(' ')
        f2.write('NONSPEECH\n')
    elif '.' in line1 and '.' == line1[0] and 'lab' not in line1:
        f2.write('.\n') 
    else:
        line2 = line1.split()
        f2.write(line2[0])
        f2.write(' ')
        f2.write(line2[1])
        f2.write(' ')
        f2.write('SPEECH\n')
f1.close
f2.close            
