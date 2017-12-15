#!/usr/bin/python
#translate stm file to mlf file

import os,sys
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py STMFile MLFFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

ctm=sys.argv[1]
mlf=sys.argv[2]

ctmfile=open(ctm,'r')
mlffile=open(mlf,'w')

index=0
mlffile.write('#!MLF!#\n')
while True:
    index+=1
    line=ctmfile.readline()
    if not line:
       break
    else:
       temp=line.split(' ')
       if index==1:
          preaudioid=temp[0]
          print preaudioid
          title='"'+'*/'+preaudioid+'.lab'+'"'
          mlffile.write(title)
          mlffile.write('\n')
       else:
          preaudioid=audioid
       audioid=temp[0]
       channelid=temp[1]
       startpoint=str(int(round(float(temp[2])*10000000)))
       endpoint=str(int(round(float(temp[3])*10000000)))
       classid=temp[4]
       if audioid!=preaudioid:
          mlffile.write('.\n')
          title='"'+'*/'+audioid+'.lab'+'"'
          duration=startpoint+' '+endpoint+' '+classid
          mlffile.write(title)
          mlffile.write('\n')
          mlffile.write(duration)
          mlffile.write('\n')      
       else:
          endpoint=str(int(float(startpoint)+float(endpoint)))
          duration=startpoint+' '+endpoint+' '+classid
          mlffile.write(duration)
          mlffile.write('\n')
mlffile.write('.\n')
mlffile.close()
 

