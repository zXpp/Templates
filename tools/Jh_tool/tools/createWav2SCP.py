#!/usr/bin/python
# This script is to merge segment SCP files into one whole SCP file
# write these lines into another SCP file
#
import os,sys
scp1 = open('/share/spandh.ami1/usr/yanxiong/tnet.tbl.sad/tbl.full.files/tbl.plp.scp','r')
scp2 = open('/share/spandh.ami1/usr/yanxiong/tnet.tbl.sad/tbl.full.files/wav2fbank.scp','wa')
string1 ='/share/spandh.ami1/dia/bbc/tbl/audio/complete/'
string2 ='/share/spandh.ami1/usr/yanxiong/data/tbl.full.fbank/fbank/'
numofletter = 13
while True:
    line = scp1.readline()
    if not line:
        break
    scp2.write(string1)
    scp2.write(line[:13])
    scp2.write('.wav')
    scp2.write('  ')
    scp2.write(string2)
    scp2.write(line[:13])
    scp2.write('.fbk')  
    scp2.write('\n')
scp1.close
scp2.close            
