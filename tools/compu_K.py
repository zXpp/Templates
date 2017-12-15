#!/usr/bin/python
# this script is to compute the acp asp of the result from k-means.N.j

import os,os.path,sys,math,operator
#coding=utf-8
#rootdir='/home/zzpp220/DATA/TRAIN/630/630clu_/'
#for parent,dirnames,filenames in os.walk(rootdir):
#	#print filenames
#	for clu in filenames:
#		print clu
clu = sys.argv[1]
f = open(clu,'r')
clures = clu[0 : clu.find('.')]
cluresname=clures+'.k.res'
f2=open(cluresname,'wa')
fid=f.readlines()
num_sample=60
count_dict = {}
for line in fid[0:len(fid)-1]:		
	line = line.strip()
	count = count_dict.setdefault(line, 0)
	count += 1
	count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
###sorted_count_dict =[('3', 12), ('15', 10), ('9', 4), ('2', 4)]
#for item in count_dict:
y=[]
for item in sorted_count_dict:
	#print int(item[0])
	y.append((int(item[0]),item[1]))
	#
	#f2.write( "%s ------> %d\n" % (item[0], item[1]))
#print sorted(sorted_count_dict,key=lambda x:(x[0],x[0].lower()))
print sorted(y)	
for tup in sorted(y):
	f2.write("%s ------> %d\n" % (tup[0], tup[1]))



    
f2.close
f.close




