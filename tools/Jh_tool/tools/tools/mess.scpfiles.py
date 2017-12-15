#!/usr/bin/python
# This script is to transform phonems list in one MLF into SPEECH/NONSPEECH list and then
# write these SPEECH/NONSPEECH into another MLF file
#
import os,sys
f0 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16','r')
f1 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.1','wa')
f2 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.2','wa')
f3 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.3','wa')
f4 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.4','wa')
f5 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.5','wa')
f6 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.6','wa')
f7 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.7','wa')
f8 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.8','wa')
f9 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.9','wa')
f10 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07_fbank_scp/rt07.fbank.scp.train16.10','wa')
iter = 1
while True:
    line1 = f0.readline()
    if not line1:
        break
    temp1 = iter % 10
    if temp1 == 1:
        f1.write(line1)
    if temp1 == 2:
        f2.write(line1)
    if temp1 == 3:
        f3.write(line1)
    if temp1 == 4:
        f4.write(line1)
    if temp1 == 5:
        f5.write(line1)
    if temp1 == 6:
        f6.write(line1)
    if temp1 == 7:
        f7.write(line1)
    if temp1 == 8:
        f8.write(line1)
    if temp1 == 9:
        f9.write(line1)
    if temp1 == 0:
        f10.write(line1)
    iter = iter + 1    
    print iter
f0.close
f1.close
f2.close      
f3.close
f4.close
f5.close
f6.close
f7.close
f8.close
f9.close
f10.close
