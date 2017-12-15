#!/usr/bin/python
# This script is to find text string extracted from one file in other file
#
#
import os,sys
scp1 = open('/share/spandh.ami1/usr/yanxiong/tnet.sad.fbank/tbl.full.testdata.fbank.scp','r')
while True:
    line1 = scp1.readline()
    if not line1:
        break
    temp1 = line1[:10]
    mlf1 = open('/share/spandh.ami1/usr/yanxiong/tnet.sad.fbank/test_ref.mlf.new','r')
    while True:
        line2 = mlf1.readline()
        if line2.find(temp1) == -1: # if not found
           flag = 0
        else:
            flag = 1
            break
        if not line2:
            if flag == 0:
                print temp1
            break
    mlf1.close
scp1.close
mlf1.close
