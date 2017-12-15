#!/usr/bin/python
# # This script is to generate scp lines according to one MLF file
#
import os,sys
if len(sys.argv) != 4:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py MLFFile PathOfFeatureFiles SuffixName"
    print "\nSuffixName is the suffix of feature files, e.g. fbk, bn, plp, mfc"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

file1 = sys.argv[1]
mlf = open(file1,'r')
while '/' in file1:
    file1 = file1[file1.find('/')+1 : len(file1)]  # delete '/'
file2 = file1[0 : file1.find('.')]
print file1
print file2

scp = open(file2 + '.scp','w')
path = sys.argv[2] + '/'
suffix = sys.argv[3]

#StartPoint_B = 31 # start point of one segment
#StartPoint_E = 38 # start point of one segment
#EndPoint_B = 39   # end point of one segment
#EndPoint_E = 46   # end point of one segment
iter = 1 # number of Seg files
while True:
    line1 = mlf.readline() # read one line
    if not line1:
        break
    if 'lab' in line1:
	 filename = line1[3 : line1.rfind('.')]
     	 scp.write(filename)
     	 scp.write('.'+suffix+'=')
     	 scp.write(path)
     	 scp.write(filename) 
     	 scp.write('.'+suffix+'\n')

        # extract startpoint of one segment
       # startpoint = line1[StartPoint_B:StartPoint_E] # extract start point of one segment
       # while True:
       #     if int(startpoint) == 0: # if startpoint equal to 0
       #         startpoint = '0'
       #         break
       #     elif startpoint[:1] == '0': # if the first letter is 0
       #         startpoint = startpoint[1:len(startpoint)] # delete the first letter
       #     else:
       #         break
       # # extract endpoint of one segment
       # endpoint = line1[EndPoint_B:EndPoint_E] # extract end point of one segment
       # while True:
       #     if int(endpoint) == 0: # if endpoint equatl to 0
       #         endpoint = '0'
       #         break
       #     elif endpoint[:1] == '0': # if the first letter is 0
       #         endpoint = endpoint[1:len(endpoint)] # delete the first letter
       #     else:
       #         break
       # segname = line1[3:46]
       # filename = line1[3:20]
       # scp.write(segname)
       # scp.write('.'+suffix+'=')
       # scp.write(path)
       # scp.write(filename) 
       # scp.write('.'+suffix+'[')
       # scp.write(startpoint)
       # scp.write(',')
       # scp.write(endpoint)
       # scp.write(']\n')   
mlf.close
scp.close            
