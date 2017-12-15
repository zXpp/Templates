#!/usr/bin/python
#
import os,sys,math
string = 'chain83'
path = '/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/textgrid'
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
        label = line4_temp[2]
        label = label[1:] # delete the first "
        label = label[:-1]
        label=label[label.find('_')+1:label.find('_train')]
        f2.write('%s\n' % label)
#             sys.exit()
f2.write('.\n')   # write the last line
f1.close
f2.close
