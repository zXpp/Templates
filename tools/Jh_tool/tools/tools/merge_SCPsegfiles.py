#!/usr/bin/python
# This script is to merge segment SCP files into one whole SCP file
# write these lines into another SCP file
#
import os,sys
scp1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-ami.sad.fbank/nn.386.1000.1000.1000.1000.2.fbank.train.hmm100/ami.test.fbank.scp','r')
line1 = scp1.readline() # read the first line
scp2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-ami.sad.fbank/nn.386.1000.1000.1000.1000.2.fbank.train.hmm100/ami.test.fbank.scp.new','wa')
scp2.write(line1) # write the first line
num = 0
numofletter = 16
filename1 = line1[:numofletter] # extract file name
#print filename1 # print file name
while True:
    line1 = scp1.readline()
    if not line1:
        break
    if filename1 != line1[:numofletter]: # not belong to the same file
        filename1 = line1[:numofletter] # update file name
        scp2.write(line1) # write a line 
scp1.close
scp2.close            
