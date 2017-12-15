#!/usr/bin/python
#
import os,sys,math,re
#string = 'chain83'
path = '/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/SCUTPHONE/textgrid'
#file1 = path + '/%s.TextGrid' % string
file2 = path + '2test.mlf'
f2 = open(file2, 'wa',0)
f2.write('#!MLF!#\n')

def mlf_dir(string,f1,f2):   # write the first line
##string is the filename without the suffix .ex chain66.TextGrid ,string=chain66
##f1 is the single TextGrid file,ex.chain66.TextGrid fileflag,read each line one time,f2 is the destination mlf file flag
    f2.write('"*/%s.lab"\n' % string) # write the second line
#    iter = 0
#    lastlabel =''
    while True:
        line1 = f1.readline()
        if not line1:
            break
        elif 'intervals [' in line1:
            line2 = f1.readline()
            line2_temp = line2.split()
            sp = str(int(round(float(line2_temp[2]) * 10000000)))   # change start point
            f2.write(sp) # write start point     
            f2.write(' ')   # write a space
            line3 = f1.readline()
            line3_temp = line3.split()
            ep = str(int(round(float(line3_temp[2]) * 10000000)))   # change end point
            f2.write(ep) # write end point
            f2.write(' ')   # write a space
            line4 = f1.readline()
            line4_temp = line4.split()
            label = line4_temp[2]
            label = label[1:] # delete the first "
            label = label[:-1]
            
#            set=re.split('[\W+_\d+]',label) ##
#            for ele in label_set:
#                if ele in set:
#                    label=ele
            
            label=label[label.find('_')+1:label.find('_test')]
            f2.write('%s\n' % label)
            #             sys.exit()
           # write the last line
        f1.close

label_set=['wind','Rivers','Rain','Male','Female','gunshots','drums','birds','bass','babies','applause']

for file in os.walk(path,True):
    textname_list=file[2]
    for textgrid_file in textname_list:
        if '.TextGrid' in textgrid_file:
            total_file=os.path.join(path,textgrid_file)
            f1 = open(total_file, 'r')
            non_suffix=textgrid_file[0:textgrid_file.find('.TextGrid')]
            mlf_dir(non_suffix,f1,f2)
            f2.write('.\n')
        else:
            print "{} is not a TextGrid file".format(textgrid_file)
f2.close

