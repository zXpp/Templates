#!/usr/bin/python
#translate stm file to mlf file

import os,sys,re
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py MFCCFile MLFFile "
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

mfcc=sys.argv[1]
scp=sys.argv[2]
try:
    mfccfile=open(mfcc,'r')
    scpfile=open(scp,'w')
except IOError as ioerr:
    print("io error:{0}".format(ioerr))

index=0
startpoint=0
while True:
    mfccline=mfccfile.readline()
    if not mfccline:
        break
    else:
        if  mfccline.find('[')!=-1:
            #temp=re.match(r'(\w+)_([a-z]+)(\d+)',mfccline)
            #audioid=temp.group(1)+'_'+temp.group(2)+temp.group(3)
            #classid=temp.group(2)
            #print audioid,classid,'\n'
            #index=0
            startpoint=index+1
            continue
        else:
            index+=1
            if mfccline.find(']')!=-1:
                print index,'\n'
                endpoint=index
                #titleline='"*/'+audioid+'.lab"\n'
                refline='chain_'+str(startpoint)+'_'+str(endpoint)+'=../data/chain.fea['+str(startpoint)+','+str(endpoint)+']'+'\n'
                #mlffile.write(titleline)
                scpfile.write(refline)
                #scpfile.write('.\n')
            else:
                continue
mfccfile.close()
scpfile.close()

