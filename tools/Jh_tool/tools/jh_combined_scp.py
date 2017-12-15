#!/usr/bin/python
# This script is to generate scp lines int HCopy , attention it will read all .wav file include 
# sub-dirtory!  
#
import os,sys
if len(sys.argv) != 6:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py WavPath FeaturePath SuffixName Scpfile"
    print "\nSuffixName is the suffix of feature files, e.g. fbk, bn, plp, mfc"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

path_wav = sys.argv[1]
path_feat = sys.argv[2]
SuffixName1 = sys.argv[3]
SuffixName2 = sys.argv[4]
text = sys.argv[5]

scp = open(text + '.scp','w')

for dirpath, dirnames, filenames in os.walk(path_wav):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ('.'+ SuffixName1) :
                filepath = os.path.join(dirpath, filename)
                scp.write(filepath)

                filename = filename[0 : filename.rfind('.')]
                scp.write(' '+path_feat)
                scp.write('/'+ filename)
                scp.write('.'+ SuffixName2 + '\n')

                print("file:" + filepath)
                input_file = open(filepath)
                text = input_file.read()
                input_file.close()

                output_file = open( filepath, 'w')
                output_file.write(text)
                output_file.close()
scp.close

