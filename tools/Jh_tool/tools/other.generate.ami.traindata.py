#!/usr/bin/python
# This script is to generate a new segment MLF files by merging detail labs in the old MLF file
#
import os,sys
mlf1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.sad.fbank/train.mlf','r')
line1 = mlf1.readline() # read the first line
mlf2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.sad.fbank/train.mlf.new','wa')
mlf2.write(line1) # write the first line
StartPoint_B = 20 # start point of one segment begining at the 21th letter
StartPoint_E = 26 # start point of one segment ending at the 26th letter
EndPoint_B = 27   # end point of one segment begining at the 28th letter
EndPoint_E = 33   #  end point of one segment ending at the 33th letter
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
        # write current line
        mlf2.write(line1)
        mlf2.write('0') # write start point
        mlf2.write(' ')
        mlf2.write(str(int(endpoint) - int(startpoint)))
#       mlf2.write(str(int(endpoint) - int(startpoint) + 1))
        mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
        mlf2.write(' ')
        line2 = mlf1.readline() # read one line
        line3 = line2.split()
        mlf2.write(line3[2])
        mlf2.write('\n')
        mlf2.write('.\n')
mlf1.close
mlf2.close            
