# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 20:59:49 2016

@author: zzpp220
"""
import os,sys
from os import listdir
from os.path import isfile, join

bn_path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/bn/gmsv/208_1024_1024_13_21_2520cat'#sys.argv[1] 
bn_files = [ f for f in listdir(bn_path) if (isfile(join(bn_path,f)) and 'train_chain393.bn.array' in f)] ##only files under the dir
#bn_label='train_chain'+*+r'.bn.array'  format in eachline:S3 2.7812 2.7106 0.61578 2.4145 3.0493 3.0668'
#nbn_label='train_chain393.bn'

ref_path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chainv3.0/train/ref_rttm/' #sys.argv[2]
ref_files = [ f for f in listdir(ref_path) if (isfile(join(ref_path,f)) and 'train_chain393.ref.rttm' in f)] ##only files under the dir
#ref_label='train_chain393'+r'.ref.rttm'
bn_total=r'train_chain393tot.bn.array'
#sys.argv[3] 
nbn=open(os.path.join(bn_path,bn_total),'w')

brandlist=['Apple_iPhone5','HTC_Desire_c','HTC_Sensation_xe','LG_GS290','LG_L3','LG_Optimus_L5','LG_Optimus_L9','Nokia_5530','Nokia_C5','Nokia_N70',
'Samsung_E1230','Samsung_E2121B','Samsung_E2600','Samsung_Galaxy_GT-I9100_s2','Samsung_Galaxy_Nexus_S','Samsung_Gt-I8190_mini','Samsung_Gt-N7100',
'Samsung_S5830i','Sony_Ericson_c510i','Sony_Ericson_c902','Vodafone_joy_845']
id=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
sprid=dict(zip(brandlist,id))

if len(bn_files)==len(ref_files):
    filenum=len(bn_files)
    for i in range(filenum):
        ref=open(os.path.join(ref_path,ref_files[i]),'r')
        ref_base=ref_files[i].split('.')[0] ##train_chain390
        for bn_e in bn_files:
            if ref_base in bn_e: ##train_chain390 in train_chain390.bn.array
                bn=open(os.path.join(bn_path,bn_e),'r') ##substring in 
                
                #nbn_sep=open(os.path.join(bn_path,ref_base+'.bn.array'),'w')        
                    ##############################################
                index=0    
                while True:
                    line1 = ref.readline()
                    line2 = bn.readline()
                    if (not line1) or (not line2):
                        break
                    brand=line1.split()[7] ##Apple_iPhone5
                    name=line2.split(' ',1) #['S3', '2.7812 2.7106 0.61578 2.4145 3.0493 3.0668']
                    
                    if brand in sprid.keys():
                        newname='S'+str(index)+'#'+sprid[brand]+' '+name[0] #S3#A
                        nbn.write(newname+' '+name[1])
                    index+=1    
ref.close()
bn.close()
nbn.close()
