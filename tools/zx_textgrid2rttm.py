#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file

from os import path


#if len(sys.argv) != 2:
#   print "\n USAGE: scriptname TextGridfile"
#   sys.exit()
textgridpath=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/chain6.0/14cellphones/textgrid'
file1 =path.join(textgridpath,'cells_test_chain432.TextGrid') #sys.argv[1]
file2 = file1
file2=path.split(file2)[1]
file2 = file2[0 : file2.find('.')]
file2name = file2
file2 = path.join(textgridpath,file2+'.ref.rttm')

f1 = open(file1, 'r')
f2 = open(file2, 'wa')
#f2.write(';;This is an RTTM file. Each record contains 9 whitespace separated fields:\n')   # write the first line
#f2.write(';;1:type	2:file		3:chnl		4:tbe		5:tdur		6:ortho		7:subtype	8:spkrname	9:conf\n') # write the second line
#f2.write(';SPKR-INFO FileName	1	<NA>	<NA>	<NA>	unknown	SpeakerName	<NA>\n')
iter = 0
lastlabel =''
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'intervals [' in line1:
        line2 = f1.readline()
        line2_temp = line2.split()
        sp = str(line2_temp[2])   # change start point

        if '_train' in file2name:# "Samsung_s5830i_train2" -->Samsung_s5830i
        		file2name_new=file2name[0:file2name.find('_train')]
        else:
             file2name_new=file2name
             flg_test=True
        f2.write('SPEAKER %s 1 ' % file2name)	
        f2.write('%.6s' % sp) # write start point     
        f2.write(' ')   # write a space
        line3 = f1.readline()
        line3_temp = line3.split()
        dur = str(float(line3_temp[2]) - float(line2_temp[2]))   # duration
        f2.write(dur) # write duration
        line4 = f1.readline()
        line4_temp = line4.split()
        label = line4_temp[2]
        label = label[1:] # delete the first "
        label = label[:-1] # delete the last "
        if flg_test:
            label = label[label.find('_')+1:label.rfind('_test')]
        else:
            label = label[0:label.rfind('_train')]
        f2.write(' <NA>	<NA> %s	<NA>\n' % label)
f1.close
f2.close
