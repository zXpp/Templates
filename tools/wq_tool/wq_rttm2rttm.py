#!/usr/bin/python
#translate stm file to mlf file

import os,sys
if len(sys.argv)!=4:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py refRTTMFile sysRTTMFile MLFFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

refrttm=sys.argv[1]
sysrttm=sys.argv[2]
mlf=sys.argv[3]

refrttmfile=open(refrttm,'r')
sysrttmfile=open(sysrttm,'r')
rttmfile=open(mlf,'w')

while True:
    refrttmline=refrttmfile.readline()
    sysrttmline=sysrttmfile.readline()
    if not refrttmline or not sysrttmline:
        break
    else:
        systemp=sysrttmline.split(' ')
        reftemp=refrttmline.split(' ')
        writeline=refrttmline.replace(reftemp[-2],systemp[-2])
        rttmfile.write(writeline) 
refrttmfile.close()
sysrttmfile.close()
rttmfile.close()
 

