#!/usr/bin/python
# This script is to merge segment MLF files into one whole MLF file
# write these lines into another MLF file
#
import os,sys
mlf1 = open('/share/spandh.ami1/usr/yanxiong/data/wka.full.fbank/wka.sad.mlf.notmerge','r')
line1 = mlf1.readline() # read the first line
mlf2 = open('/share/spandh.ami1/usr/yanxiong/data/wka.full.fbank/wka.sad.mlf.temp','wa')
mlf2.write(line1) # write the first line
numofletter = 24 # 16 for TBL dataset, 24 for WKA dataset. the first 16 letter of file name
NoofFinLett = -6 #the last letter is the ENTER symbol
StartPoint_B = 27 # 26 for TBL, 27 for WKA.  start point of one segment begining at the 27th letter
StartPoint_E = 33 # start point of one segment ending at the 33th letter
EndPoint_B = 34   # end point of one segment begining at the 35th letter
EndPoint_E = 40   #41 for TBL, 40 for WKA.  end point of one segment ending at the 41th letter
filename1 = 'randomletters' # initialize one string randomly
iter = 1 # number of Seg files
while True:
    line1 = mlf1.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
        # extract startpoint of one segment
        startpoint = line1[StartPoint_B:StartPoint_E] # extract start point of one segment
        while True:
            if int(startpoint) == 0: # if startpoint equal to 0
                startpoint = '0'
                break
            elif startpoint[:1] == '0': # if the first letter is 0
                startpoint = startpoint[1:len(startpoint)] # delete the first letter
            else:
                break
        # extract endpoint of one segment
        endpoint = line1[EndPoint_B:EndPoint_E] # extract end point of one segment
        while True:
            if int(endpoint) == 0: # if endpoint equatl to 0
                endpoint = '0'
                break
            elif endpoint[:1] == '0': # if the first letter is 0
                endpoint = endpoint[1:len(endpoint)] # delete the first letter
            else:
                break
        # read another line
        line2 = mlf1.readline() # read the next line in mlf file1
        if 'NONSPEECH' in line2:
            string = 'NONSPEECH'
        elif 'SPEECH' in line2  and 'NONSPEECH' not in line2:
            string = 'SPEECH'
        # verify whether new file starts or not
        if filename1 != line1[:numofletter]: # not belong to the same file
            if iter != 1:
                mlf2.write('.') # write a line only containing one dot
                mlf2.write('\n')
            else:
                iter = 0
            mlf2.write(line1[:numofletter]) # write the first numofletter letters for file name
            mlf2.write(line1[NoofFinLett:]) # write the last NoofFinLett letter for file name
            filename1 = line1[:numofletter] # update variable for storing file name
            if int(startpoint) != 0:  
                mlf2.write('0')
                mlf2.write(' ')
                mlf2.write(startpoint)
                mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
                mlf2.write(' ')
                if string == 'SPEECH':
                    mlf2.write('NONSPEECH')
                elif string == 'NONSPEECH':
                    mlf2.write('SPEECH')
                mlf2.write('\n')
        if int(startpoint) < int(endpoint):  # startpoint < endpoint
            mlf2.write(startpoint) # write start point
            mlf2.write('00000') # add 5 zero behind of startpoint as the final start point
            mlf2.write(' ')
            mlf2.write(endpoint)
            mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
            mlf2.write(' ')
            mlf2.write(string) # write SPEECH or NONSPEECH into new MLF file
            mlf2.write('\n')
mlf2.write('.') # write a line only containing one dot
mlf1.close
mlf2.close           
