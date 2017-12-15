# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:36:51 2017

@author: zzpp220
"""
import os,os.path
import numpy as np

path=r'/media/zzpp220/Data/Linux_Documents/Mobile/DATA/Total_TestData/SCUTPHONE'
brandfile='brandnamelist.txt'
concatewav='/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/scut_test_chain430'

brandlist=list(np.loadtxt(os.path.join(path,brandfile),dtype=str))
value=range(15)

map_dict=dict(zip(brandlist,value))
mapvalue=[]
for root, dirs, wavlists in os.walk(concatewav,topdown=True):
    for wavfiles in wavlists:
        if ".wav" in wavfiles:
            brandname=wavfiles[wavfiles.find('_')+1:wavfiles.rfind('_')]
            if brandname in map_dict.keys():
                mapvalue.append(map_dict[brandname])
            else:
                print wavfiles
parr=np.array(mapvalue)
parr.tofile(os.path.join(concatewav,"scut_test_chain430_lab2int.txt"),sep="\n",format="%s")
print parr