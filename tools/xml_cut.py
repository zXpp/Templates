# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:21:54 2016

@author: zzpp220
"""
import os,sys,math

def dim_row(array_name,iter_index):
    if '<dimension>' in array_name[iter_index]:
        array_name[iter_index]='    <dimension>'+str(dim)+'</dimension>\n'
    elif '<numRows>50</numRows>' in array_name[iter_index]:
        array_name[iter_index]='        <numRows>'+str(dim)+'</numRows>\n'
def row_col(array_name,iter_index): 
    if '<numRows>50</numRows>' in array_name[iter_index]:
        array_name[iter_index]='        <numRows>'+str(dim)+'</numRows>\n'
    elif '<numCols>50</numCols>' in array_name[iter_index]:
        array_name[iter_index]='        <numCols>'+str(dim)+'</numCols>\n'

#def iter_mean_cov():
dim_commend=sys.argv[1]
dim=int(dim_commend)
     
path='/home/zzpp220/Documents/LIUM-master/mat/'
fread=open(path+'wld.efn_50.xml','r')
fwrite=open(path+'wld.efn_'+dim_commend+'.xml','wa')

total=fread.readlines() 
####global mean and covariance
global_head=total[0:(22+dim)]#[0:22+dim]header=22,select 17dim of 50
end_mean=total[72:84] # configs between </data> of mean and <data> of cov 

for num in range(22):
    dim_row(global_head,num)
fwrite.writelines(ele_golbal_mean for ele_golbal_mean in global_head)       


for num in range(12):
    row_col(end_mean,num)
fwrite.writelines(ele_golbal_cov for ele_golbal_cov in end_mean)

covariance=total[84:(84+2500)] #cov values
col=[]
for i in range(dim):
    col.insert(i,covariance[50*i:50*(i+1)])
    fwrite.writelines(golbal_cov_Data for golbal_cov_Data in col[i][0:dim])

list1_pass=total[2584:2597] 
for num in range(13):
    dim_row(list1_pass,num)
fwrite.writelines(ele_pass for ele_pass in list1_pass)   

#####list iternation #####

iter=[]
for iter_index in range(5):
    begin=(2597+5105*iter_index)
    end=2597+5105*(iter_index+1)
    iter.insert(iter_index,total[begin:end])
    iter_tmp=iter[iter_index]
#for i in range(5):
    ####head and mean 17 data
    #iter_tmp=iter[i]
    iter_head_mean=iter_tmp[0:(22+dim)]
    for num_head in range(22):        
        dim_row(iter_head_mean,num_head)
    fwrite.writelines(ele_iter_head_mean for ele_iter_head_mean in iter_head_mean)
    
    ###configs between end of mean and head of cov
    iter_mean_2_cov=iter_tmp[72:84]
    for num in range(12):
        row_col(iter_mean_2_cov,num)
    fwrite.writelines(ele_iter_mean_2_cov for ele_iter_mean_2_cov in end_mean)
    
    ##select dim*dim datas from original cov matrix
    covariance=iter_tmp[84:(84+2500)] #cov values
    iter_col=[]
    for p in range(dim):
        iter_col.insert(p,covariance[50*p:50*(p+1)])
        fwrite.writelines(iter_cov_Data for iter_cov_Data in iter_col[p][0:dim])
    
    ###configs between end of cov and head of t 
    iter_cov_2_t=iter_tmp[2584:2601] 
    for num in range(17):
        row_col(iter_cov_2_t,num)
    fwrite.writelines(ele_iter_cov_2_t for ele_iter_cov_2_t in iter_cov_2_t)
    
    ##elect dim*dim datas from original t matrix
    covariance_t=iter_tmp[2601:(2601+2500)] #cov values
    iter_col_t=[]
    for q in range(dim):
        iter_col_t.insert(q,covariance_t[50*q:50*(q+1)])
        fwrite.writelines(iter_cov_Data for iter_cov_Data in iter_col_t[q][0:dim])
    
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
fread.close
fwrite.close      
        
