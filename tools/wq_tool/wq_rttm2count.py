#!/usr/bin/python
#translate stm file to mlf file

import os,sys
if len(sys.argv)!=4:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py refRTTMFile sysRTTMFile COUNTFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

refrttm=sys.argv[1]
sysrttm=sys.argv[2]
mlf=sys.argv[3]

refrttmfile=open(refrttm,'r')
sysrttmfile=open(sysrttm,'r')
countfile=open(mlf,'w')

maxcount=5
classset=['applause','cheer','fighting','gunshot','laughter','music','noise','other','rain','river','speech','wind']

for numid in range(1,maxcount+1):
    countfile.write('\tspkr_{}'.format(numid))
countfile.write('\n')
matchmatric=[]
classidlist=[]
classlist=[]
while True:
    refrttmline=refrttmfile.readline()
    sysrttmline=sysrttmfile.readline()
    if not refrttmline or not sysrttmline:
        break
    else:
        systemp=sysrttmline.split(' ')
        reftemp=refrttmline.split(' ')
        sysid=systemp[-2] 
        refid=reftemp[-2]
        if not refid in classidlist:
           classidlist.append(refid)
        matchmatric.append('{0}_{1}'.format(sysid,refid))
        classlist.append(refid)
#print matchmatric 

for tempid in classidlist:
    countfile.write('{}\t'.format(tempid))
    numofclass=classlist.count(tempid)
    print numofclass
    for num in range(1,maxcount+1):
        var='spkr_'+str(num)+'_'+tempid
        tempid_num=matchmatric.count(var)
        countfile.write('{0}/{1}\t'.format(tempid_num,numofclass))
    countfile.write('\n')
refrttmfile.close()
sysrttmfile.close()
countfile.close()
