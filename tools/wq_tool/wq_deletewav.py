#!/usr/bin/python
#This script is to generate text lines from the title of the all .wav

import os,sys
if len(sys.argv)!=2:
    print "------------------------------------------------"
    print "\nUSAGE: python  script Wavpath"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

path_wav=sys.argv[1]

deletelist=['cheer','music','wind','other','laughter','fighting','noise']

for dirpath,subdirpath,filename in os.walk(path_wav):
    for dirpaths in subdirpath:
        print dirpaths
        classpath=path_wav+os.sep+dirpaths
        for dirname,dirnames,filenamepath in os.walk(classpath):
          for filenames in filenamepath:
              print filenames
              for classid in deletelist:   
                  if filenames.find(classid)!=-1:
                     print classpath+os.sep+filenames
                     os.system('rm {}'.format(classpath+os.sep+filenames))
                  else:
                      continue
print 'done'
