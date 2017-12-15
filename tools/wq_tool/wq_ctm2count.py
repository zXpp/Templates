#!/usr/bin/python
#translate stm file to mlf file

import os,sys,re
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py ctmMFile COUNTFiles"
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

refrttm=sys.argv[1]
mlf=sys.argv[2]

refrttmfile=open(refrttm,'r')
countfile=open(mlf,'w')

maxcount=12
classset=['applause','cheer','fighting','gunshot','laughter','music','noise','other','rain','river','speech','wind']

for numid in classset:
    countfile.write('\t{}'.format(numid))
countfile.write('\n')

matchmatric=[]

while True:
    refrttmline=refrttmfile.readline()
    if not refrttmline :
        break
    else:
        reftemp=refrttmline.split(' ')
        sysid=reftemp[4] 
        ref=reftemp[0]
        temp=re.match(r'(\w+)_([a-z]+)(\d+)',ref)
        refid=temp.group(2) 
        matchmatric.append('{0}_{1}'.format(sysid,refid))
print matchmatric 

for tempid in classset:
    countfile.write('{}\t'.format(tempid))
    for num in classset:
        var=num.upper()+'_'+tempid
        print var
        tempid_num=matchmatric.count(var)
        countfile.write('{}\t'.format(tempid_num))
    countfile.write('\n')
refrttmfile.close()
countfile.close()
