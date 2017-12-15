#!/usr/bin/python
# This script is to transform phonems list in one MLF into SPEECH/NONSPEECH list and then
# write these SPEECH/NONSPEECH into another MLF file
#
import os,sys
filename = sys.argv[1]
f1 = open(filename,'r')
f2 = open(filename + '.ForAlign','wa')
f2.write('#!MLF!#\n')
while True:
    line = f1.readline()
    if not line:
        break
    if '.rec' in line:
        fn = line[0:16]  # file name
    elif ' SPEECH' in line:
        line1 = line.split()
        temp1 =  str(int(line1[0])/100000)
        while True:
            if len(temp1) < 6:
                temp1 = '0' + temp1
            else:
                break
        seg_s =  temp1

        temp1 =  str(int(line1[1])/100000)
        while True:
            if len(temp1) < 6:
                temp1 = '0' + temp1
            else:
                break
        seg_e =  temp1
        line = fn + '_' + seg_s + '_' + seg_e + '.lab"\n'
        f2.write(line)
        f2.write('SPEECH\n')
        f2.write('.\n')


f1.close
f2.close
