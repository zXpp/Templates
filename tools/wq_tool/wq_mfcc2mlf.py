#!/usr/bin/python
#translate stm file to mlf file

import os,sys,re
if len(sys.argv)!=3:
    print "------------------------------------------------"
    print "\nUSAGE: python  script.py MFCCFile MLFFile "
    print "\n---------- Error!! --------------------------------------"
    sys.exit()

mfcc=sys.argv[1]
mlf=sys.argv[2]

mfccfile=open(mfcc,'r')
mlffile=open(mlf,'w')

num=-1
index=0
mlffile.write('#!MLF!#\n')
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
            index=0
            continue
        else:
            index+=1
            if mfccline.find(']')!=-1:
                print index,'\n'
                duration=index*100000
                titleline='"*/'+audioid+'.lab"\n'
                refline='0 '+str(duration)+' '+classid+'\n'
                mlffile.write(titleline)
                mlffile.write(refline)
                mlffile.write('.\n')
            else:
                continue
mlffile.close()
mfccfile.close()

