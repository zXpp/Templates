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
            continue
        else:
            index+=1     
            if mfccline.find(']')!=-1:
                nos=mfccline.find(']')
                mfccline=mfccline[0:nos]+'\n'
                scpfile.write(mfccline)
            else:
                scpfile.write(mfccline)
                continue
mfccfile.close()
scpfile.close()

