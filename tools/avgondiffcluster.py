# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:31:08 2017

@author: zzpp220
"""
from pandas import DataFrame
import pandas as pd
import os
'''该脚本用于用tot2520的文件生成一个自定义类数的中心文件，除不尽的话剩下的样本数都加到最后一组以便送入k_means。用之前，必须先对２５２０ｔｏｔ进行shuf'''
dir_path='/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-dnn/208.500.500.26.21-26-256'
tot_filename='3rd_shuf_26-256.txt'
speaker_num=21
center_filename='shuf-208-500-500-26-21-26-256cen'+str(speaker_num)+'.txt'



sample_percluster=2520//speaker_num
#sample_percluster=120
tot_Cat=pd.read_table(os.path.join(dir_path,tot_filename),sep='	',header=None,names=None)
tot_Cat=tot_Cat.dropna(how='all',axis=1)
#fid=open(dir_path+'cluster_changed.txt','w')
res=[]
for i in range (speaker_num):
    if i==speaker_num-1:
        cluster=tot_Cat[sample_percluster*i:].mean()
    else:
        cluster=tot_Cat[sample_percluster*i:sample_percluster*(i+1)].mean()
#    cluster.to_csv
    res.append(cluster)
tot_data=DataFrame(res)
##write center data to txt file
tot_data.to_csv(os.path.join(dir_path,'shuf_clustercenter_test',str(speaker_num),center_filename),sep=' ',index=False,header=False)
#fid.close()