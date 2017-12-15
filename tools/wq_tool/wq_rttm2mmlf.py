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
mlffile=open(mlf,'w')
#matchfile=open('/home/winky/match.txt','w')

index=0
mlffile.write('#!MLF!#\n')
while True:
    refrttmline=refrttmfile.readline()
    sysrttmline=sysrttmfile.readline()
    if not refrttmline or not sysrttmline:
        break
    else:
        index+=1
        reftemp=refrttmline.split()
        refend=float(reftemp[4])*10000000
        if (refend-0.0)<0.00000001 and (0.0-refend)>-0.00000001:
            print 'error:duration is zero!',index
            sys.exit()
        else:
            refend=str(refend) 
        systemp=sysrttmline.split()
        sysid=systemp[-2] 
        refid=reftemp[-2]
        title='"*/'+str(index)+'.lab"'+'\n' 
        writeline='0 '+refend+' '+sysid+'\n'
        mlffile.write(title)
        mlffile.write(writeline) 
        mlffile.write('.\n')
        '''
        refrttmline=refrttmline.replace(refid,sysid)
        mlffile.write(refrttmline)
        matchfile.write(refid+'_'+sysid+'\n')
        '''
refrttmfile.close()
sysrttmfile.close()
mlffile.close()
#matchfile.close()
 

