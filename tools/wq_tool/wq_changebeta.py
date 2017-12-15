#!/usr/bin/python

import os,sys,re

if len(sys.argv)!=2:
    print 'please input beta which to be changed!'

changebeta=sys.argv[1]
print changebeta
readfilepath='/home/winky/spkr_diar_copy/config/ib.cfg'
writefilepath='/home/winky/spkr_diar_copy/config/ib_copy.cfg'

readfile=open(readfilepath,'r')
writefile=open(writefilepath,'w')

while True:
    line=readfile.readline()
    if not line:
        break
    else:
        if line.find('AIB_BETA')!=-1:
            matchtemp=re.match(r'(\w+)=(\d+)(.*)',line)
            beta=matchtemp.group(2)
            print beta,str(changebeta)
            line=line.replace(beta,str(changebeta))
            print line
            writefile.write(line)
        else:
            writefile.write(line)
            continue
readfile.close()
writefile.close()

