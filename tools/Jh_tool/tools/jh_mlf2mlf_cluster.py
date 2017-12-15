#!/usr/bin/python
# # This script is to generate rec  according to one MLF file,used in htk
#
import os,sys
if len(sys.argv) != 2:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py MLFFile"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

file1 = sys.argv[1]
mlf = open(file1,'r')
while '/' in file1:
    file1 = file1[file1.find('/')+1 : len(file1)]  # delete '/'
file2 = file1[0 : file1.find('.')]
print file1
print file2

flag = 0;
mlf_cluster = open(file2 + '_cluster.mlf','w')

iter = 1 # number of Seg files
while True:
    line1 = mlf.readline() # read one line
    if not line1:
        break
    if '#!MLF#' in line1:
	 continue
    if 'rec' in line1:
	 filename = line1[3 : line1.rfind('.')]
     	 filename += '.rec'
	 print filename
	 mlf_cluster.write('"*/'+ filename + '"')
	 mlf_cluster.write('\n')
	 
    	 line1 = mlf.readline() # read one line
	 dict1 = {}#creat dict
	 while line1 != '.\n': 
	     str_split = line1.split(' ')
	     print str_split[2]
	     if dict1.has_key(str_split[2]):
		dict1[str_split[2]] = dict1[str_split[2]] + (int(str_split[1]) - int(str_split[0]))
	     else:
		dict1[str_split[2]] = int(str_split[1]) - int(str_split[0])
	     print dict1[str_split[2]]
    	     line1 = mlf.readline() # read one line
	
	 max = 0
	 total = 0
	 max_key = ''	
	 for key in dict1:
	     total = total + dict1[key]
	     if max_key == '':
	 	max = dict1[key]
		max_key = key
	        continue
	     if dict1[key] > max:
	 	max = dict1[key]
		max_key = key
	 
	 mlf_cluster.write('0 ')
	 mlf_cluster.write('%d' %total)
	 mlf_cluster.write(' ' + max_key + '\n.\n')	   

mlf_cluster.close		
mlf.close
