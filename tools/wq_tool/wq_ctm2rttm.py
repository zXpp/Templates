#!/usr/bin/python
#translate stm file to mlf file

import os,sys
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py STMFile MLFFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

ctm=sys.argv[1]
rttm=sys.argv[2]

ctmfile=open(ctm,'r')
rttmfile=open(rttm,'w')

index=0
endtime=0
while True:
    index+=1
    line=ctmfile.readline()
    if not line:
       break
    else:
       temp=line.split(' ')
       starttime=endtime
       durtime=temp[3]
       endtime+=float(durtime)+0.01
       classid=temp[4]
       refline='SPEAKER chain 1 '+str(starttime)+' '+str(durtime)+' <NA> <NA> '+classid+' '+'<NA>'+'\n'
       rttmfile.write(refline)
ctmfile.close()
rttmfile.close()
 

