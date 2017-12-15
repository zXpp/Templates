# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:33:127_10 2016

@author: zzpp220
"""

#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

import os,sys


#if len(sys.argv) != 3:
#   print "\n USAGE: scriptname TextGridfile newchainname"
#   sys.exit()

file1='/media/zzpp220/Data/Linux_Documents/mobile/chain/newchain/chain90/chain90.TextGrid'
#file1 = sys.argv[1]
#filename_tmp=os.path.basename(file1)
#filename_tmp2=filename_tmp.split(".")
#filename='new'+filename_tmp2
#newchaindir=sys.argv[2]
newchaindir='/media/zzpp220/Data/Linux_Documents/mobile/chain/newchain/newchain90'
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
        i+=1
        label_index=str(i)+'_'+label
        if os.path.exists(label):
            #shutil.copyfile(label,"~/newchain60/label_index")
            #m=label_index
           os.environ['label']=str(label)
           os.environ['label_index']=str(label_index)
           os.environ['newchaindir']=str(newchaindir)
           #os.system("cp -a $label ~/newchain60/$label_index")
           os.system("cp -a $label $newchaindir/$label_index")
            #os.system("mv ~/newchain60/")
       # os.system("if label in '/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/WAV2520/")
        
            
