#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

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
cluresname=clures+'.res'
f2=open(cluresname,'wa')
fid=f.readlines()
num_sample=30
for i in range(0,21):
	p=i+1
	count_dict = {}
	f2.write("----------------\n")
	f2.write("num:%d\n" %i)
	for line in fid[num_sample*i:num_sample*p]:		
		line = line.strip()
		count = count_dict.setdefault(line, 0)
		count += 1
		count_dict[line] = count
	sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
	for item in sorted_count_dict:
		f2.write( "%s ------> %d\n" % (item[0], item[1]))	
	f2.write("******************\n")
	f2.write(" \n")
f2.close
f.close
