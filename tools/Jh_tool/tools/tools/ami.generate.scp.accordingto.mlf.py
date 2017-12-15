#!/usr/bin/python
# # This script is to generate scp lines according to one MLF file
#
import os,sys
mlf = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/cv.mlf','r')
scp = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/cv.fbank.scp','wa')
path = '/share/spandh.ami1/asr/dev/mtg/ac/exp.nn/ihm/data/ac/fbk23/'
StartPoint_B = 20 # start point of one segment begining at the 21th letter
StartPoint_E = 26 # start point of one segment ending at the 26th letter
EndPoint_B = 27   # end point of one segment begining at the 28th letter
EndPoint_E = 33   #  end point of one segment ending at the 33th letter
iter = 1 # number of Seg files
while True:
    line1 = mlf.readline() # read one line
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
        segname = line1[3:33]
        filename = line1[3:19]
        scp.write(segname)
        scp.write('.fbk=')
        scp.write(path)
        scp.write(filename) 
        scp.write('.fbk[')
        scp.write(startpoint)
        scp.write(',')
        scp.write(endpoint)
        scp.write(']\n')   
mlf.close
scp.close            
