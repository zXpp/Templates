#!/usr/bin/python
#
import os,sys,math
string = 'chain'
path = '/home/winky'
path1 = '/home/winky'
file1 = path + '/%s.TextGrid' % string
file2 = path1 + '/%s.mlf.lab' % string
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
	if 'Nonspeech' in line4 and line4_temp[2] == '"Nonspeech"':
	    print iter
	    iter = int(iter) + 1
	    f2.write('Nonspeech\n') # write label
	    if int(iter) == 1:
		lastlabel = 'Nonspeech'
	    else:
		if lastlabel == 'Nonspeech':
		    print iter
		    print 'ERROR1 !'
	    lastlabel = 'Nonspeech'
	elif 'spkr_0' in line4 and line4_temp[2] == '"spkr_0"':   
	    iter = int(iter) + 1
	    f2.write('spkr_0\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_0'
	    else:
		if lastlabel == 'spkr_0':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_0' 
	elif 'spkr_1' in line4 and line4_temp[2] == '"spkr_1"':   
	    iter = int(iter) + 1
	    f2.write('spkr_1\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_1'
	    else:
		if lastlabel == 'spkr_1':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_1' 
	elif 'spkr_2' in line4 and line4_temp[2] == '"spkr_2"':   
	    iter = int(iter) + 1
	    f2.write('spkr_2\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_2'
	    else:
		if lastlabel == 'spkr_2':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_2' 
	elif 'spkr_3' in line4 and line4_temp[2] == '"spkr_3"':   
	    iter = int(iter) + 1
	    f2.write('spkr_3\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_3'
	    else:
		if lastlabel == 'spkr_3':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_3' 
	elif 'spkr_4' in line4 and line4_temp[2] == '"spkr_4"':   
	    iter = int(iter) + 1
	    f2.write('spkr_4\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_4'
	    else:
		if lastlabel == 'spkr_4':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_4' 
        elif 'spkr_5' in line4 and line4_temp[2] == '"spkr_5"':   
	    iter = int(iter) + 1
	    f2.write('spkr_5\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_5'
	    else:
		if lastlabel == 'spkr_5':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_5' 
        elif 'spkr_6' in line4 and line4_temp[2] == '"spkr_6"':   
	    iter = int(iter) + 1
	    f2.write('spkr_6\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_6'
	    else:
		if lastlabel == 'spkr_6':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_6' 
        elif 'spkr_7' in line4 and line4_temp[2] == '"spkr_7"':   
	    iter = int(iter) + 1
	    f2.write('spkr_7\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_7'
	    else:
		if lastlabel == 'spkr_7':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_7' 
        elif 'spkr_8' in line4 and line4_temp[2] == '"spkr_8"':   
	    iter = int(iter) + 1
	    f2.write('spkr_8\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_8'
	    else:
		if lastlabel == 'spkr_8':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_8' 
        elif 'spkr_9' in line4 and line4_temp[2] == '"spkr_9"':   
	    iter = int(iter) + 1
	    f2.write('spkr_9\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_9'
	    else:
		if lastlabel == 'spkr_9':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_9' 
        elif 'spkr_10' in line4 and line4_temp[2] == '"spkr_10"':   
	    iter = int(iter) + 1
	    f2.write('spkr_10\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_10'
	    else:
		if lastlabel == 'spkr_10':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_10' 
        elif 'spkr_11' in line4 and line4_temp[2] == '"spkr_11"':   
	    iter = int(iter) + 1
	    f2.write('spkr_11\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_11'
	    else:
		if lastlabel == 'spkr_11':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_11' 
        elif 'spkr_12' in line4 and line4_temp[2] == '"spkr_12"':   
	    iter = int(iter) + 1
	    f2.write('spkr_12\n') # write label
	    if int(iter) == 1:
		lastlabel = 'spkr_12'
	    else:
		if lastlabel == 'spkr_12':
		    print iter
		    print 'ERROR2 !'
	    lastlabel = 'spkr_12' 
	else:
	     f2.write('SN\n') # leak label
	     print iter
	     print 'ERROR3 !'
#             sys.exit()
f2.write('.\n')   # write the last line
f1.close
f2.close
