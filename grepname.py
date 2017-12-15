# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:33:45 2016

@author: zzpp220
"""

#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

import os,sys,math


#if len(sys.argv) != 2:
#   print "\n USAGE: scriptname TextGridfile"
#   sys.exit()

#file1 = sys.argv[1]
file1='/media/zzpp220/Data/Linux_Documents/mobile/chain/newchain/chian60/chain60.TextGrid'
file2 = file1
while '/' in file2:
    file2 = file2[file2.find('/')+1 : len(file2)]  # delete '/'
file2 = file2[0 : file2.find('.')]
file2name = file2
file2 = './' + file2 + '.ref.rttm'

f1 = open(file1, 'r')
f2 = open(file2, 'wa')
iter = 0
lastlabel =''
i=0
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'intervals [' in line1:
        line2 = f1.readline()
        line3 = f1.readline()
        line4 = f1.readline()
        line4_temp = line4.split()
        label = line4_temp[2]
        label = label[1:] # delete the first "
        label = label[:-1]+'.wav'
        label_index=str(i+1)+'_'+label
        if label in '/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/WAV2520/':
            os.system("cp -a /media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/WAV2520/label ~/newchain60/")
            os.system("mv ~/newchain60/")
       # os.system("if label in '/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/WAV2520/")
        
            