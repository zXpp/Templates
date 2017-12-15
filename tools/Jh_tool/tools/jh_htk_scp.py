#!/usr/bin/python
# This script is to generate scp lines int HCopy , attention it will read all .wav file include 
# sub-dirtory!  
#
import os,sys
if len(sys.argv) != 4:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py FeatPath SuffixName Scpfile"
    print "\nSuffixName is the suffix of feature files, e.g. fbk, bn, plp, mfc"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

path_feat = sys.argv[1]
SuffixName = sys.argv[2]
text = sys.argv[3]

scp = open(text + '.scp','w')

for dirpath, dirnames, filenames in os.walk(path_feat):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ('.' + SuffixName):
                filepath = os.path.join(dirpath, filename)
                #scp.write(filepath)

                filename = filename[0 : filename.rfind('.')]
                scp.write(' '+path_feat)
                scp.write('/'+ filename)
                scp.write('.'+ SuffixName + '\n')

                print("file:" + filepath)
                input_file = open(filepath)
                text = input_file.read()
                input_file.close()

                output_file = open( filepath, 'w')
                output_file.write(text)
                output_file.close()
scp.close

