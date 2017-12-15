#!/usr/bin/python
#
import os,sys

if len(sys.argv) < 2:
    print "------------------------------------------------"
    print "\nUSAGE: python  calculate_length_of_speech_and_nonspeech_fullfiles.py  FullPathOfMLFFile CorpusName"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()
elif len(sys.argv) == 3:
    CorpusName = sys.argv[2]

f1 = open(sys.argv[1],'r')

nonspeechlen = 0
speechlen = 0
numofspeech = 0
numofnonspeech = 0
iter = 0
SegName = ' '
while True:
    if len(sys.argv) == 2:
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
    elif len(sys.argv) == 3:
        line1 = f1.readline()
        if not line1:
            break
        elif ' SPEECH' in line1 and CorpusName in SegName:
            line2 = line1.split()
            duration1 = int(line2[1]) - int(line2[0])
            numofspeech = int(numofspeech)+int(1)
            speechlen = int(speechlen) + int(duration1)
            iter = int(iter) + 1
        elif ' NONSPEECH' in line1 and CorpusName in SegName:
            line3 = line1.split()
            duration2 = int(line3[1]) - int(line3[0])
            numofnonspeech = int(numofnonspeech) + 1
            nonspeechlen = int(nonspeechlen) + int(duration2)
            iter = int(iter) + 1
        elif '.lab' in line1:
            SegName = line1

temp1 = float(speechlen)/float(10000000*3600)
print('Speech: %.3f h, ' % temp1)
#print float(speechlen)/10000000
print('%s Segments.' % numofspeech)
#print numofspeech

temp1 = float(nonspeechlen)/(10000000*3600)
print('\nNonspeech: %.3f h, ' % temp1)
#print float(nonspeechlen)/10000000
print('%s Segments' % numofnonspeech)
#print numofnonspeech

print('\n%s Segments, ' % iter)
#print iter
temp1  = (float(speechlen)+float(nonspeechlen))/(10000000*3600)
print('%.3f h, in total.' % temp1)
#print (float(speechlen)+float(nonspeechlen))/10000000
temp1 = float(speechlen)/(float(speechlen)+float(nonspeechlen))
temp2 = float(nonspeechlen)/(float(speechlen)+float(nonspeechlen))
print('Portions of SPEECH to NONSPEECH: %.3f : ' % temp1)

#print float(speechlen)/(float(speechlen)+float(nonspeechlen))
print('%.3f.' % temp2)
#print float(nonspeechlen)/(float(speechlen)+float(nonspeechlen))

f1.close
