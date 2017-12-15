#!/usr/bin/python
# this script is to transform SCP file to RTTM file

import os,sys,math,re
file1=sys.argv[1]
f1 = open(file1, 'r')
try:
	l1=f1.read()
finally:
	f1.close()
#print str

#savedstdout=sys.stdout
#with open ('/home/zzpp220/Documents/score/reference.list','w+') as file:
#	sys.stdout=file
#	print f1.name

#sys.stdout=savedstdout

basname=os.path.basename(f1.name)#chain6_6.scp
tmpname=basname.split('.')[0]#chain6_6
mseg=tmpname+'.m_gai.seg'#chain6_6.m.seg
f2=open(mseg,'wa')
c=0 
# mind the "["and "]" are special in regular express ,need \
result = re.findall("\[(\d+),(\d+)\]",l1) 
#print result
for line in result:
	f2.write(';; cluster S%d\n' % c)
	dur=str(int(line[1])-int(line[0]))
	dur1=str(int(dur)+1)
	if c==0:
		f2.write("%s 1 %s %s U U U S%d\n"%(tmpname,line[0],dur,c))
	else:
		start1=str(int(line[0])-1)
		f2.write("%s 1 %s %s U U U S%d\n"%(tmpname,start1,dur1,c))
		#print start1,line[0]
	c+=1

f2.close()
#
nseg=basname.split('.')[0]+'.n.seg'
f3=open(nseg,'wa')
f3.write(';; cluster init\n' )

f= open(file1, 'r')
d =f.readlines()[len(f.readlines())-1]
last=re.findall("\[(\d+),(\d+)\]",d)
#print last
f3.write('%s 1 0 %s U U U init\n'%(tmpname,last[0][1]))
f3.close()
f.close()









