# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:47:56 2016

@author: zzpp220
"""
'''this script is to find the coor segments according to the samplelist from the 2520tot_cat gmsv to make the train_chain{393,```445},after trainefr and computmaha ,then run the script---sep_mobile.py'''
import os,string

brand_tmp=open(r'/media/zzpp220/Data/Linux_Documents/Mobile/DATA/Total_TestData/SCUTPHONE/brandnamelist.txt','r')
brandname=brand_tmp.readlines() #['HONGMI_1S\n', 'HONGMI_NOTE\n', 'HTC_G10\n', 'HUAWEI_P6\n',……]
brand_tmp.close()
brandlist=[string.replace(s,'\n','') for s in brandname]
#['Apple_iPhone5','HTC_Desire_c','HTC_Sensation_xe','LG_GS290','LG_L3','LG_Optimus_L5','LG_Optimus_L9','Nokia_5530','Nokia_C5','Nokia_N70',
#'Samsung_E1230','Samsung_E2121B','Samsung_E2600','Samsung_Galaxy_GT-I9100_s2','Samsung_Galaxy_Nexus_S','Samsung_Gt-I8190_mini','Samsung_Gt-N7100','Samsung_S5830i','Sony_Ericson_c510i','Sony_Ericson_c902','Vodafone_joy_845']
id=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
id=id[0:len(brandlist)]
gmsv_path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/bn_gmsv/bn_gmsv8'
label=r'scut-208-500-500-13-21-8tot_cat'
gmsv_totwrite=label+'.bn.array'
gmsv_read=label+'.txt'
bn=open(os.path.join(gmsv_path,gmsv_read),'r',0)
nbn=open(os.path.join(gmsv_path,gmsv_totwrite),'w',0)
each_mod,file_eachmod=[],[]
file_cat=open(os.path.join(gmsv_path,'scut-208-500-500-13-21file_cat.txt'),'r',0)

file_list=file_cat.readlines()
read=bn.readlines()
bn.close()
file_cat.close()

for i in range(len(brandlist)):
    p=i+1
    file_eachmod.append(file_list[120*i:120*p])
    each_mod.append(read[120*i:120*p])


coor=dict(zip(brandlist,zip(each_mod,file_eachmod)))
sprid=dict(zip(brandlist,id))

snumber=[430,442,458,470]
#name='S'
for number in snumber:
    ref=open('/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/samplelist/sample_list'+str(number)+'.txt','r')
    tmp=open(os.path.join(gmsv_path,'scut_test_chain'+str(number)+'.bn.array'),'w',0)
    index=0
    
    while True:
        line=ref.readline()
        if not line:
            break
        line_testtmp=os.path.basename(line).split('.wav') #['Vodafone_joy_845_test22', '\n']
        line_tmp=line_testtmp[0].split('_test') #['Vodafone_joy_845', '22']
        line_mod=line_tmp[0] #'Vodafone_joy_845'
        num=int(line_tmp[1]) #22
        
        if line_mod in coor.keys():
            bn_line_tmp=coor[line_mod][0] #120 sample filename
            bn_file_tmp=coor[line_mod][1] #120 bngmsv line coor to filename
            coor_file=[f for f in bn_file_tmp if (line_testtmp[0] in f)]
            bn_line_coorindex=bn_file_tmp.index(coor_file[0])
            bn_line=bn_line_tmp[bn_line_coorindex]
            name='S'+str(index) # bn array is to send to ilp ,no need to label their coor speakerid  +'#'+sprid[line_mod]
            tmp.write(name+' '+bn_line)#.split(' ',1)[0])
            nbn.write(name+'#'+sprid[line_mod]+' '+bn_line)#.split(' ',1)[0])
        index+=1
        
    ref.close()
    tmp.close()
nbn.close()    