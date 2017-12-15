# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:58:42 2016

@author: zzpp220
"""
''' this script is to seperate the tot.efr.y output from trainefr into the cooresponde num in file'''
import re,os

snumber=[430,442,458,470]
path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/bn_gmsv/bn_gmsv8'
tot_efr=open(os.path.join(path,'scut-208-500-500-13-21-8tot_cat.efr_52.y'),'r')
for num in snumber:
    flag=open(os.path.join(path,'scut_test_chain'+str(num)+'.efr.y'),'w')
    
    for line in range(num):
        line_coor=tot_efr.readline()
        line_nolabel=re.sub('#\w','',line_coor)
        flag.write(line_nolabel)
    flag.close()
tot_efr.close()