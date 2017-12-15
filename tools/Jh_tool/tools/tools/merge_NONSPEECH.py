#!/usr/bin/python

import os,sys
oldfile = '/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/ami.SpeechNonspeech.mlf'
newfile = '/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/ami.SpeechNonspeech.mlf.new'
f = open(oldfile,'r')
nf = open(newfile,'wa')
num = 1
while True:
    line = f.readline()
    if 'NONSPEECH' in line:
        line = line.split()
        if num == 1:
            nf.write(line[0])
            nf.write(' ')
            endtime = line[1]
            contents = line[2]
            num = num + 1
        else:
            endtime = line[1]
            contents = line[2]
    elif not line:
        break
    else:
        if num > 1:
            nf.write(endtime)
            nf.write(' ')
            nf.write(contents)
            nf.write('\n')
        num = 1
        nf.write(line)
f.close
nf.close
