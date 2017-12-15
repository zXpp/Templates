#!/usr/bin/python
import os,os.path,sys,math,operator
#coding=utf-8
resfile= sys.argv[1]
f=open(resfile,'r')
line=f.readlines()[len(f.readlines())-1]
print line
