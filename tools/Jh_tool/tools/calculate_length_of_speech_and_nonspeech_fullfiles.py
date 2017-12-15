#!/usr/bin/python
#
import os,sys
filename = 1201
# calculate length from FULL FILE!!!!
#f1 = open('/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.asrsns/cv.mlf','r')
#f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.sad.fbank/cv.mlf','r')

f1 = open('/share/spandh.ami1/usr/yanxiong/data/rt07/reference/rt07.mlf/rt07.auto1.ihm.sns.complete.mlf.16files','r')


#f1 = open('/share/spandh.ami1/usr/yanxiong/data/tbl.new/TBL%s-MIXA1.mlf' % filename,'r')
nonspeechlen = 0
speechlen = 0
numofspeech = 0
numofnonspeech = 0
iter = 0
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif ' SPEECH' in line1:
        line2 = line1.split()
        duration1 = int(line2[1]) - int(line2[0])
        numofspeech = int(numofspeech)+int(1)
        speechlen = int(speechlen) + int(duration1)
        iter = int(iter) + 1
    elif ' NONSPEECH' in line1:
        line3 = line1.split()
        duration2 = int(line3[1]) - int(line3[0])
        numofnonspeech = int(numofnonspeech) + 1
        nonspeechlen = int(nonspeechlen) + int(duration2)
        iter = int(iter) + 1
print('speech length is:'),  float(speechlen)/float(10000000)
#print float(speechlen)/10000000
print('speech num is: %s' % numofspeech)
#print numofspeech

print('\nnonspeech length is: '), float(nonspeechlen)/10000000
#print float(nonspeechlen)/10000000
print('nonspeech num is: %s' % numofnonspeech)
#print numofnonspeech

print('\nsegment number in total: %s' % iter)
#print iter
print('duration in total (seconds): '), (float(speechlen)+float(nonspeechlen))/10000000
#print (float(speechlen)+float(nonspeechlen))/10000000
print('Portions of SPEECH: '), float(speechlen)/(float(speechlen)+float(nonspeechlen))

#print float(speechlen)/(float(speechlen)+float(nonspeechlen))
print('Portions of NONSPEECH: '), float(nonspeechlen)/(float(speechlen)+float(nonspeechlen))
#print float(nonspeechlen)/(float(speechlen)+float(nonspeechlen))

f1.close
