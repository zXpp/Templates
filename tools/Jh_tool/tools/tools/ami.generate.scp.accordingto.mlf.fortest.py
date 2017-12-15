#!/usr/bin/python
# # This script is to generate scp lines according to one MLF file
#
import os,sys
mlf = open('/share/spandh.ami1/usr/yanxiong/data/ami.full.fbank/ami.sad.mlf','r')
scp = open('/share/spandh.ami1/usr/yanxiong/data/ami.full.fbank/ami.fbank.scp','wa')
path = '/share/spandh.ami1/usr/yanxiong/data/ami_fbk/'
while True:
    line1 = mlf.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
        filename = line1[3:33]
        scp.write(filename)
        scp.write('.fbk=')
        scp.write(path)
        scp.write(filename) 
        scp.write('.fbk\n')
mlf.close
scp.close            
