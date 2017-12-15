#!/usr/bin/python
#translate stm file to mlf file

import os,sys
#if len(sys.argv)!=3:
#    print "------------------------------------------------"
#    print "\nUSAGE: python  script.py rttmFile mlfFiles"
#    print "\n---------- Error!! --------------------------------------"
#    sys.exit()

rttm='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/ref_rttm/chain66.ref.rttm'#rttm=sys.argv[1]
mlf='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain_v2.0_concate/ref_rttm/chain66.mlf'#mlf=sys.argv[2]

ctmfile=open(rttm,'r')
mlffile=open(mlf,'w')

index=0
mlffile.write('#!MLF!#\n')
while True:
    index+=1
    line=ctmfile.readline()
    if not line:
       break
    else:
       temp=line.split('\t')
       if index==1:
          preaudioid=temp[1]
          print preaudioid
          title='"'+'*/'+preaudioid+'.lab'+'"'
          mlffile.write(title)
          mlffile.write('\n')
          startpoint=int(round(float(temp[3])*10000000))
          endpoint=int(round(float(temp[4])*10000000))
          lastendpoint='0'
       else:
          preaudioid=audioid
       audioid=temp[1]
       channelid=temp[2]
       startpoint=str(int(round(float(temp[3])*10000000)))
       endpoint=str(int(round(float(temp[4])*10000000)))
       classid=temp[7]
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
          duration=lastendpoint+' '+endpoint+' '+classid
          lastendpoint=endpoint
          mlffile.write(duration)
          mlffile.write('\n')
mlffile.write('.\n')
mlffile.close()
 

