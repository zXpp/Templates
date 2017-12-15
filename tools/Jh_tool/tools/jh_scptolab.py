#!/usr/bin/python
# # This script is to generate lab  according to one MLF file,used in htk
#
import os,sys
if len(sys.argv) != 3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py MLFFile PathOfLabFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

file1 = sys.argv[1]
mlf = open(file1,'r')
while '/' in file1:
    file1 = file1[file1.find('/')+1 : len(file1)]  # delete '/'
file2 = file1[0 : file1.find('.')]
print file1
print file2

path = sys.argv[2]
flag = 0;

iter = 1 # number of Seg files
while True:
    line1 = mlf.readline() # read one line
    if not line1:
        break
    if '#!MLF#' in line1:
	 continue
    if 'lab' in line1:
	 filename = line1[3 : line1.rfind('.')]
     	 filename += '.lab'
	 lab = open(path + '/' + filename,'w')
	 flag = 1
    if flag == 1:
	 if '.' in line1:
		lab.close
    	 else:
         	lab.write(line1)
mlf.close
