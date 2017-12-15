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
duration=0
while True:
    mfccline=mfccfile.readline()
    if not mfccline:
        break
    else:
        if  mfccline.find('[')!=-1:
            temp=re.match(r'(\w+)_([a-z]+)(\d+)',mfccline)
            audioid=temp.group(1)+'_'+temp.group(2)+temp.group(3)
            classid=temp.group(2)
            print audioid,classid,'\n'
            startpoint=index+1
            continue
        else:
            index+=1
            duration+=1
            if mfccline.find(']')!=-1:
                print index,'\n'
                #endpoint=index
                refline='SPEAKER chain 1 '+str(float(startpoint)/100)+' '+str(float(duration)/100)+' <NA> <NA> '+classid+' '+'<NA>'+'\n'
                scpfile.write(refline)
                duration=0
            else:
                continue
mfccfile.close()
scpfile.close()

