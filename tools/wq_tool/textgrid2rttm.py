#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

import os,sys,math


if len(sys.argv) != 2:
   print "\n USAGE: scriptname TextGridfile"
   sys.exit()

file1 = sys.argv[1]
file2 = file1
while '/' in file2:
    file2 = file2[file2.find('/')+1 : len(file2)]  # delete '/'
file2 = file2[0 : file2.find('.')]
file2name = file2
file2 = './' + file2 + '.rttm'

f1 = open(file1, 'r')
f2 = open(file2, 'wa')
f2.write(';;This is an RTTM file. Each record contains 9 whitespace separated fields:\n')   # write the first line
f2.write(';;1:type	2:file		3:chnl		4:tbe		5:tdur		6:ortho		7:subtype	8:spkrname	9:conf\n') # write the second line
f2.write('SPKR-INFO FileName	1	<NA>	<NA>	<NA>	unknown	SpeakerName	<NA>\n')
iter = 0
lastlabel =''
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'intervals [' in line1:
        line2 = f1.readline()
        line2_temp = line2.split()
        sp = str(line2_temp[2])   # change start point
	f2.write('SPEAKER	%s	1	' % file2name)
        f2.write(sp) # write start point     
        f2.write('	')   # write a space
        line3 = f1.readline()
        line3_temp = line3.split()
        dur = str(float(line3_temp[2]) - float(line2_temp[2]))   # duration
        f2.write(dur) # write duration
        line4 = f1.readline()
        line4_temp = line4.split()
	label = line4_temp[2]
	label = label[1:] # delete the first "
	label = label[:-1] # delete the last "
	f2.write('	<NA>	<NA>	%s	<NA>\n' % label)
f1.close
f2.close
