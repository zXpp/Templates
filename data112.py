# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:18:01 2017

@author: zzpp220
"""
import numpy as np
import os,os.path,sys
from pandas import DataFrame,Series
import pandas as pd
brandnamelist=["Apple_iPhone5","HTC_Desire_c","HTC_Sensation_xe","LG_GS290","LG_L3","LG_Optimus_L5","LG_Optimus_L9","Nokia_5530","Nokia_C5","Nokia_N70","Samsung_E1230","Samsung_E2121B","Samsung_E2600","Samsung_Galaxy_GT-I9100_s2","Samsung_Galaxy_Nexus_S","Samsung_Gt-I8190_mini","Samsung_Gt-N7100","Samsung_S5830i","Sony_Ericson_c510i","Sony_Ericson_c902","Vodafone_joy_845"]

modelnum=21#the speaker type)
clu = '/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256/shuf_clustercenter_test/18/shuf-208-500-500-26-21-26-256-clu.txt'
f = open(clu,'r')
clu_basename=os.path.basename(clu)
clu_dir=os.path.dirname(clu)
clures = clu_basename[0 : clu_basename.find('.')]
cluresname=clures+'.res' #630_21.res
njname=clures+'.k.res' 
chart_file=os.path.join(clu_dir,clures+'.xls')#630_21.k.res
f3=open(os.path.join(clu_dir,njname),'wa')
f2=open(os.path.join(clu_dir,cluresname),'wa')
fid=f.readlines()
list=[]
for i in range(modelnum):
    list.append(Series(fid[120*i:120*(i+1)]))
data=DataFrame(list)