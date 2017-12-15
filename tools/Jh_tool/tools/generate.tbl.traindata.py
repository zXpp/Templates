#!/usr/bin/python
# This script is to generate a new segment MLF files by merging detail labs in the old MLF file
#
import os,sys
mlf1 = open('/share/spandh.ami1/usr/yanxiong/tnet.tbl-tbl.sad.fbank/train.mlf','r')
line1 = mlf1.readline() # read the first line
mlf2 = open('/share/spandh.ami1/usr/yanxiong/tnet.tbl-tbl.sad.fbank/train.mlf.new','wa')
mlf2.write(line1) # write the first line
numofletter = 17 # 16 for TBL dataset. the first 16 letter of file name
NoofFinLett = -6 #the last letter is the ENTER symbol
StartPoint_B = 20 # 20 for TBL.  start point of one segment begining at the 21th letter
StartPoint_E = 27 # start point of one segment ending at the 27th letter
EndPoint_B = 28   # end point of one segment begining at the 29th letter
EndPoint_E = 35   #35 for TBL.  end point of one segment ending at the 35th letter
filename1 = 'randomletters' # initialize one string randomly
while True:
    line1 = mlf1.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
        str_filename = line1[:numofletter]
        str_ns = 'NS_'
        str_startpoint = line1[StartPoint_B:StartPoint_E]
        str_dash = '_'
        str_endpoint =  line1[EndPoint_B:EndPoint_E]
        str_lab = '.lab"'
        str_7zero = '0000000'
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
        # verify whether new file starts or not
        if filename1 != line1[:numofletter]: #  new file occur
            filename1 = line1[:numofletter] # update variable for storing file name
            if int(startpoint) != 0:
                # write silence segment name
                mlf2.write(str_filename)
                mlf2.write(str_ns)
		mlf2.write(str_7zero)
                mlf2.write(str_dash)
                mlf2.write(str_startpoint)
                mlf2.write(str_lab)
                mlf2.write('\n')
                # write start and end point of silence segment
                mlf2.write('0')
                mlf2.write(' ')
                mlf2.write(str(int(startpoint)))
#                mlf2.write(str(int(startpoint) + 1))
                mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
                mlf2.write(' ')
                mlf2.write('NONSPEECH')
                mlf2.write('\n')
                mlf2.write('.\n')
            else:
                mlf2.write(line1) # write segment name
                # write start and end point of silence segment
                mlf2.write('0')
                mlf2.write(' ')
#                mlf2.write(str(int(startpoint) + 1))
                mlf2.write(str(int(startpoint)))
                mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
                mlf2.write(' ')
                mlf2.write('SPEECH')
                mlf2.write('\n')
                mlf2.write('.\n')
            # write current line
            mlf2.write(line1) # write segment name
            # write start and end point of silence segment
            mlf2.write('0')
            mlf2.write(' ')
            mlf2.write(str(int(endpoint) - int(startpoint)))
#            mlf2.write(str(int(endpoint) - int(startpoint) + 1))
            mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
            mlf2.write(' ')
            mlf2.write('SPEECH')
            mlf2.write('\n')
            mlf2.write('.\n')   
        else:  # if belong to the same file
            if int(startpoint) > int(LastEndpoint):  # startpoint of this Seg file > endpoint of last Seg file
                # write silence segment name
                mlf2.write(str_filename)
                mlf2.write(str_ns)
                mlf2.write(str_LastEndpoint)
                mlf2.write(str_dash)
                mlf2.write(str_startpoint)
                mlf2.write(str_lab)
                mlf2.write('\n')
                # write start and end point of silence segment
                mlf2.write('0')
                mlf2.write(' ')
                mlf2.write(str(int(startpoint) - int(LastEndpoint)))
#                mlf2.write(str(int(startpoint) - int(LastEndpoint) + 1))
                mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
                mlf2.write(' ')
                mlf2.write('NONSPEECH')
                mlf2.write('\n')
                mlf2.write('.\n')
            # write current line
            mlf2.write(line1)
            mlf2.write('0') # write start point
            mlf2.write(' ')
            mlf2.write(str(int(endpoint) - int(startpoint)))
#            mlf2.write(str(int(endpoint) - int(startpoint) + 1))
            mlf2.write('00000') # add 5 zero behind of endpoint as the final end point
            mlf2.write(' ')
            mlf2.write('SPEECH')
            mlf2.write('\n')
            mlf2.write('.\n')
        LastEndpoint = endpoint # update last point
        str_LastEndpoint = str_endpoint
mlf1.close
mlf2.close            
