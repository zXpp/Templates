#!/usr/bin/python
#
import os,sys,math
string = 'car3'
path = '/home/jinhai/jh'
file1 = path + '/%s.TextGrid' % string
file2 = path + '/%s.mlf' % string
f1 = open(file1, 'r')
f2 = open(file2, 'wa')
f2.write('#!MLF!#\n')   # write the first line
f2.write('"*/%s.lab"\n' % string) # write the second line
iter = 0
lastlabel =''
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'intervals [' in line1:
        line2 = f1.readline()
        line2_temp = line2.split()
        sp = str(int(round(float(line2_temp[2]) * 10000000)))   # change start point
        f2.write(sp) # write start point     
        f2.write(' ')   # write a space
        line3 = f1.readline()
        line3_temp = line3.split()
        ep = str(int(round(float(line3_temp[2]) * 10000000)))   # change end point
        f2.write(ep) # write end point
        f2.write(' ')   # write a space
        line4 = f1.readline()
        line4_temp = line4.split()
        if 'NONSPEECH' in line4 and line4_temp[2] == '"NONSPEECH"':
            iter = int(iter) + 1
            f2.write('NONSPEECH\n') # write label
            if int(iter) == 1:
                lastlabel = 'NONSPEECH'
            else:
                if lastlabel == 'NONSPEECH':
                    print iter
                    print 'ERROR1 !'
            lastlabel = 'NONSPEECH'
        elif 'SPEECH' in line4 and line4_temp[2] == '"SPEECH"':   
            iter = int(iter) + 1
            f2.write('SPEECH\n') # write label
            if int(iter) == 1:
                lastlabel = 'SPEECH'
            else:
                if lastlabel == 'SPEECH':
                    print iter
                    print 'ERROR2 !'
            lastlabel = 'SPEECH' 
        else:
             print iter
             print 'ERROR3 !'
#             sys.exit()
f2.write('.\n')   # write the last line
f1.close
f2.close
