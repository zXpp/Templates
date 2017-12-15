#!/usr/bin/python
#This script is to generate text lines from the title of the all .wav

import os,sys
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script Wavpath Textfile"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

path_wav=sys.argv[1]
path_text=sys.argv[2]

scp=open(path_wav,'r')
text=open(path_text,'w')

while True:
      line=scp.readline()
      if not line:
         break
      else:
         strline=line.split('  ')
         print strline
         totclass=['applause','cheer','fighting','gunshot','laughter','music','noise','other','rain','river','speech','wind']
         for classstr in totclass:
             nos=strline[0].find(classstr)
             if nos!=-1:
               #writeline=strline[0]+'  '+'h#'+'  '+classstr+'  '+'h#'+'  '+'\n'
               #writeline=strline[0]+'  '+'sil'+'  '+classstr+'  '+'sil'+'  '+'\n'
                writeline=strline[0]+'  '+classstr+'  '+'\n'
                text.write(writeline)
             else:
               continue
text.close
print 'done'
