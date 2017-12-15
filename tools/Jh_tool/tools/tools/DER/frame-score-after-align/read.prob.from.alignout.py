#!/usr/bin/python
# This script is to transform phonems list in one MLF into SPEECH/NONSPEECH list and then
# write these SPEECH/NONSPEECH into another MLF file
#
import os,sys
import gzip
import random

def SpeakerLabel(FileName, ChannelName):
    if 'TBL06' in FileName:
        if 'CAM01' in ChannelName: 
            spkr = 'TBL06-CM-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL06-MN-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL06-SF-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL06-DW-CAM22'
    elif 'TBL09' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL09-JS-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL09-SB-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL09-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL09-KW-CAM22'
    elif 'TBL15' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL15-CD-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL15-ML-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL15-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL15-DA-CAM22'
    elif 'TBL17' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL17-HK-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL17-DM-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL17-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL17-KC-CAM22'
    elif 'TBL20' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL20-SS-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL20-KG-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL20-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL20-LB-CAM22'
    elif 'TBL21' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL21-GO-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL21-HM-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL21-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL21-RS-CAM22'
    elif 'TBL22' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL22-RA-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL22-IL-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL22-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL22-RG-CAM22'
    elif 'TBL23' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL23-LJ-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL23-PS-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL23-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL23-AG-CAM22'
    elif 'TBL24' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL24-NW-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL24-MG-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL24-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL24-AL-CAM22'
    elif 'TBL25' in FileName:
        if 'CAM01' in ChannelName:
            spkr = 'TBL25-MS-CAM01'
        elif 'CAM02' in ChannelName:
            spkr = 'TBL25-NH-CAM02'
        elif 'CAM12' in ChannelName:
            spkr = 'TBL25-ED-CAM12'
        elif 'CAM22' in ChannelName:
            spkr = 'TBL25-DJ-CAM22'
    else:
        print 'File name or Channel name are wrong1!\n'
        sys.exit()
    return spkr


#--------------------------------------------
# main
print "------------------------------------------------"
print "USAGE: python scriptname.py LOGfiles/CAM01.LOGfile LOGfiles/CAM02.LOGfile LOGfiles/CAM12.LOGfile LOGfiles/CAM22.LOGfile"
print "------------------------------------------------"
print "It is processing, please wait ......\n"
outmlf = 'spkr.mlf'
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]
f1 = gzip.open(file1, 'r')
f2 = gzip.open(file2, 'r')
f3 = gzip.open(file3, 'r')
f4 = gzip.open(file4, 'r')
f = open(outmlf, 'wa')
f.write('#!MLF!#\n')
iter = 1
lastname = ' '
set = 0
while True:
    line1 = f1.readline()
    line2 = f2.readline()
    line3 = f3.readline()
    line4 = f4.readline()
    if not line1:
        break
    if not line2:
        break
    if not line3:
        break
    if not line4:
        break
    if 'htk_post' in line1 and 'htk_post' in line2 and 'htk_post' in line3 and 'htk_post' in line4:
        flag = 0
        line1_1 = line1.split()
        line2_1 = line2.split()
        line3_1 = line3.split()
        line4_1 = line4.split()

        st = line1_1[2][14:20]
        st = int(st)     # start frame number of this segment
        et = line1_1[2][21:27] 
        et = int(et)     # end frame number of this segment
        sst = int(st) * 100000  # start time of this segment (in 100 ns)
        endtime = int(et) *100000 # end time of this segment (in 100 ns), used for stoping increasing 1
        
        fn = line1_1[2][0:13]  # read file name
        if lastname not in fn:
            lastname = fn # update file name

            if iter == 1:
                iter = iter + 1
                set = 0  # end time of this segment (in 100 ns)
            else:
                 f.write('.\n')
            f.write('"*/' + fn + '.lab"\n')
            
    elif '(SPEECH)' in line1:
        if flag == 0:
            flag = flag + 1
        else:
            sst = sst + 100000

        line1_1 = line1.split()
        line2_1 = line2.split()
        line3_1 = line3.split()
        line4_1 = line4.split()
        
        set = sst + 100000  # end time of this segment (in 100 ns)
        if set > endtime:  # set can't be larger than ent time of the segment
            set = endtime 
        prob = max(float(line1_1[6]), float(line2_1[6]), float(line3_1[6]), float(line4_1[6])) # maximum log-likelihood
        if prob == float(line1_1[6]):
            spkr =  SpeakerLabel(fn, 'CAM01')
            #spkr =  'CAM01'
        if prob == float(line2_1[6]):
            spkr =  SpeakerLabel(fn, 'CAM02')
            #spkr =  'CAM02'
        if prob == float(line3_1[6]):
            spkr =  SpeakerLabel(fn, 'CAM12')
            #spkr =  'CAM12'
        if prob == float(line4_1[6]):
            spkr =  SpeakerLabel(fn, 'CAM22')
            #spkr =  'CAM22'
        content = str(sst) + ' ' + str(set) + ' ' + spkr + ' ' + prob + '\n'
        f.write(content)
        lastendpoint = set  # update last end point
       
f1.close
f2.close
f3.close
f4.close
f.close

