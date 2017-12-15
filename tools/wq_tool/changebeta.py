#!/usr/bin/python

import os,sys,re

if len(sys.argv())!=2
    print 'please input beta which to be changed!'

changebeta=sys.argv[1]

readfilepath='/home/winky/spkr_diar_copy/config/ib.cfg'
writefilepath='/home/winky/spkr_diar_copy/config/ib_copy.cfg'

readfile.open(readfilepath)
writefile.open(writefilepath)

while True:
    line=readfile.readline()
    if not line:
        break
    else:
        if line.find('AIB_BETA')!=-1:
            matchtemp=re.match(r'(\w+)=(\d)(\s)(.*)',line)
            beta=matchtemp.group(2)
            line.replace(beta,changebeta)
            print line
            writefile.write(line)
        else:
            writefile.write(line)
            continue
readfile.close()
writefile.close()

