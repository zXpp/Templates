#!/usr/bin/python
#translate stm file to mlf file

import os,sys
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py STMFile MLFFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

stm=sys.argv[1]
mlf=sys.argv[2]

stmfile=open(stm,'r')
mlffile=open(mlf,'w')

mlffile.write('#!MLF!#\n')
while True:
    line=stmfile.readline()
    if not line:
       break
    else:
      temp=line.split(' ')
      print temp
      audioid=temp[0]
      startpoint=str(int(round(float(temp[3]) * 10000000)))
      temp2=temp[4].split('\t')
      endpoint=str(int(round(float(temp2[0]) * 10000000)))
      classid=(temp[-1]).strip()
      title='"'+'*/'+audioid+'.lab'+'"'
      duration=startpoint+' '+endpoint+' '+classid
      mlffile.write(title)
      mlffile.write('\n')
      mlffile.write(duration)
      mlffile.write('\n')
      mlffile.write('.\n')
mlffile.close
stmfile.close
      
