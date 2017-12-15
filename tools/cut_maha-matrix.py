# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:59:07 2016

@author: zzpp220
"""
##this file is to cut the file(dim=50) to file2(dim=custome)
import sys
from random import sample
dim_commend='80'
dim=int(dim_commend)
file='/home/zzpp220/Documents/LIUM-master/mat/wld.mahanalobis_50.mat'
file2='/home/zzpp220/Documents/LIUM-master/mat/wld.mahanalobis_'+dim_commend+'.mat'
flag=open(file,'r')
line1=flag.readline()
with open(file2,'wa',0) as f2:

    f2.write('%d %d MatrixSymmetric\n'%(dim,dim))
    
    if 'MatrixSymmetric' in line1:
        if dim <50:
            for i in range(dim):      
                line2=flag.readline()
            #if not line2:
             #   break
                line2_tmp=line2.split()
                line2_Cut=line2_tmp[0:dim]
            #line2_end=" ".join(line2_Cut)
                f2.write(" ".join(line2_Cut))
                f2.write('\n')
                i+=1
        else:
            dim_diff=dim-50
            total=flag.readlines()
            contain_1,contain=[],[]
            for i in range(50):
                line_3=(total[i].split('\n'))[0] ##lines with no '\n' a list with 2 strs
                #f2.writelines(line_3)
                line_3_sep=line_3.split()##seperate data a list with many strs
                contain_1=contain_1+line_3_sep ##2500 strs
                #contain_1.insert(i,line_3_sep)
                line_3_fi=' '.join(sample(contain_1,dim_diff))
                line_3_final=line_3+line_3_fi+'\n'
                #contain.insert(i,line_3_final)
                
                f2.write(line_3_final)
            for j in range(dim_diff):
                contain.insert(j,' '.join(sample(contain_1,dim)))
                f2.writelines(extra for extra in contain[j])
                f2.write('\n')
        
flag.close
#f2.close
