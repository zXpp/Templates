# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:21:54 2016

@author: zzpp220
"""
import os,sys,math
from random import sample

def dim_row(array_name,iter_index,claim_dim):
    if '<dimension>' in array_name[iter_index]:
        array_name[iter_index]='    <dimension>'+dim_commend+'</dimension>\n'
    elif '<numRows>50</numRows>' in array_name[iter_index]:
        array_name[iter_index]='        <numRows>'+dim_commend+'</numRows>\n'
def row_col(array_name,iter_index,claim_dim): 
    if '<numRows>50</numRows>' in array_name[iter_index]:
        array_name[iter_index]='        <numRows>'+dim_commend+'</numRows>\n'
    elif '<numCols>50</numCols>' in array_name[iter_index]:
        array_name[iter_index]='        <numCols>'+dim_commend+'</numCols>\n'

#def iter_mean_cov():
dim_commend='80'##sys.argv[1]
dim=int(dim_commend)-50##17
real_dim=int(dim_commend)##67
     
path='/home/zzpp220/Documents/LIUM-master/mat/'
with open(path+'wld.efn_50.xml','r')as fread:
    total=fread.readlines()
with open(path+'wld.efn_'+dim_commend+'.xml','wa',0) as fwrite:

     
    ####global mean and covariance
    global_head=total[0:22+50]#[0:22+dim]header=22,select 17dim of 50
    #total_50=total[0:22+50]
    
    
    for num in range(22):
        dim_row(global_head,num,real_dim)
    fwrite.writelines(ele_50 for ele_50 in global_head)
    fwrite.writelines(ele_golbal_mean for ele_golbal_mean in sample(total[22:(22+50)],dim))
           
    end_mean=total[72:84] # configs between </data> of mean and <data> of cov 
    
    for num in range(12):
        row_col(end_mean,num,real_dim)
    fwrite.writelines(ele_golbal_cov for ele_golbal_cov in end_mean)
    
    covariance=total[84:(84+2500)] #cov values
    col=[]
    for line in range(50):
        fwrite.writelines(golbal_cov_Data_50 for golbal_cov_Data_50 in covariance[50*line:50*(line+1)])
    #    for i in range(dim):
    #        col.insert(i,covariance[50*i:50*(i+1)])   
        fwrite.writelines(golbal_cov_Data for golbal_cov_Data in sample(covariance,dim))
    #fwrite.writelines(golbal_cov_Data_51 for golbal_cov_Data_51 in covariance[50:100])
    #fwrite.writelines(golbal_cov_Data_1 for golbal_cov_Data_1 in covariance[1500])
    fwrite.writelines(golbal_cov_Data_1 for golbal_cov_Data_1 in sample(covariance,dim*real_dim))
    
    
    list1_pass=total[2584:2597] 
    for num in range(13):
        dim_row(list1_pass,num,real_dim)
    fwrite.writelines(ele_pass for ele_pass in list1_pass)   
    
    ####list iternation #####
    
    iter=[]
    iter_total_cov=[]
    iter_total_t=[]
    for iter_index in range(5):
        begin=(2597+5105*iter_index)
        end=2597+5105*(iter_index+1)
        iter.insert(iter_index,total[begin:end])
        iter_tmp=iter[iter_index]
    #for i in range(5):
        ####head and mean 17 data
        #iter_tmp=iter[i]
        iter_head_mean=iter_tmp[0:(22+50)]
        for num_head in range(22):        
            dim_row(iter_head_mean,num_head,real_dim)
        fwrite.writelines(ele_iter_50 for ele_iter_50 in iter_head_mean)
        fwrite.writelines(ele_iter_head_mean for ele_iter_head_mean in sample(iter_tmp[22:(22+50)],dim))
        
        ###configs between end of mean and head of cov
        iter_mean_2_cov=iter_tmp[72:84]
        for num in range(12):
            row_col(iter_mean_2_cov,num,real_dim)
        fwrite.writelines(ele_iter_mean_2_cov for ele_iter_mean_2_cov in end_mean)
        
        ##select dim*dim datas from original cov matrix
        covariance_iter=iter_tmp[84:(84+2500)] #cov values
        #iter_col=[]
        iter_total_cov+=covariance_iter
        for line_1 in range(50):
            fwrite.writelines(iter_cov_Data_50 for iter_cov_Data_50 in covariance_iter[50*line_1:50*(line_1+1)])
    #    for i in range(dim):
    #        col.insert(i,covariance[50*i:50*(i+1)])   
            fwrite.writelines(iter_cov_Data for iter_cov_Data in sample(iter_total_cov,dim))
    #    fwrite.writelines(iter_cov_Data_51 for iter_cov_Data_51 in covariance_iter[50:100])
        fwrite.writelines(iter_cov_Data_1 for iter_cov_Data_1 in sample(iter_total_cov,dim*real_dim))
    #    for p in range(dim):
    #        iter_col.insert(p,covariance[50*p:50*(p+1)])
    #        fwrite.writelines(iter_cov_Data_50 for iter_cov_Data_50 in iter_col[p])
    #        fwrite.writelines(iter_cov_Data for iter_cov_Data in iter_col[p][0:dim])
    #    fwrite.writelines(iter_cov_Data_extra for iter_cov_Data_extra in iter_col[0])
    #    fwrite.writelines(iter_cov_Data_extra for iter_cov_Data_extra in iter_col[0][0:dim])   
     
        ###configs between end of cov and head of t 
        iter_cov_2_t=iter_tmp[2584:2601] 
        for num in range(17):
            row_col(iter_cov_2_t,num,real_dim)
        fwrite.writelines(ele_iter_cov_2_t for ele_iter_cov_2_t in iter_cov_2_t)
        
        ##elect dim*dim datas from original t matrix
        covariance_t=iter_tmp[2601:(2601+2500)] #cov values
        #iter_col_t=[]
        iter_total_t+=covariance_t
        for line_t in range(50):
            fwrite.writelines(iter_t_Data_50 for iter_t_Data_50 in covariance_t[50*line_t:50*(line_t+1)])
    #    for i in range(dim):
    #        col.insert(i,covariance[50*i:50*(i+1)])   
            fwrite.writelines(iter_t_Data for iter_t_Data in sample(iter_total_t,dim))
        fwrite.writelines(iter_t_Data_51 for iter_t_Data_51 in sample(iter_total_t,dim*real_dim))
    #    fwrite.writelines(iter_t_Data_1 for iter_t_Data_1 in covariance_t[1200])
    #    for q in range(dim):
    #        iter_col_t.insert(q,covariance_t[50*q:50*(q+1)])
    #        fwrite.writelines(iter_cov_Data_50 for iter_cov_Data_50 in iter_col_t[q])
    #        fwrite.writelines(iter_cov_Data for iter_cov_Data in iter_col_t[q][0:dim])
    #    fwrite.writelines(iter_cov_Data_extra for iter_cov_Data_extra in iter_col_t[0])
    #    fwrite.writelines(iter_cov_Data_extra for iter_cov_Data_extra in iter_col_t[0][0:dim])
        
        ###config after t matrix
        fwrite.writelines(last for last in iter_tmp[5101:5105])
       
    ##last sequences
    fwrite.writelines(end_last for end_last in total[28122:28124])
    #while True:
    #    line=fread.readline()
    #    if not line:
    #        break
    #    elif '<mean>' not in line:
    #        fwrite.write(line)
    #        fwrite.write('\n')
    #    elif '<mean>' in line:
    #        fwrite.write(line) #<mean>
    #        fwrite.write(fread.readline())#<mat>
            
            
#    fread.close
#    fwrite.close