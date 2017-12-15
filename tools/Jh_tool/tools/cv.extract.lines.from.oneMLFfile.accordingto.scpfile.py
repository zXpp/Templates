#!/usr/bin/python
# This script is to extract lines in MLF file according to one SCP file, and then
# write these lines into another MLF file
# this script is to extract lines of one MLF file according to SCP file, and then write these lines into
# another MLF file
import os,sys
scp1 = open('/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.sns/cv.fbank.scp','r')
mlf2 = open('/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.sns/cv.mlf','wa')
mlf2.write('#!MLF!#\n') # write the first line of mlf file
num = 0
numofletter = 30 #for AMI data, length of file name in SCP file
while True:
    num = num + 1
    print num
    line1 = scp1.readline()
    if not line1:
        break
    temp1 = line1[:numofletter]
    mlf1 = open('/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.sns/align_acftrain_SPEECH_NONSPEECH.mlf','r')
    while True:
        line2 = mlf1.readline()
        if not line2.find(temp1) == -1: # if found
           mlf2.write(line2)
           while True:
               line2 = mlf1.readline()
               if '*'  in line2: # if not reach next mlf file (the mlf file start with "*)
                   break
               elif not line2:
                   break
               else:
                   mlf2.write(line2)          
        if not line2:
            break
    mlf1.close
scp1.close
mlf1.close
mlf2.close            
