#!/usr/bin/python
#
# this script is to delete DN segments who have only one NONSPEECH line
import os,sys

# calculate length from FULL FILE!!!!
f1 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/train.mlf','r')
line = f1.readline()
f2 = open('/share/spandh.ami1/usr/yanxiong/tnet.ami-tbl.new/train.mlf.new','wa')
f2.write(line)
DN = int(35050)
iter = int(0)
while True:
    line1 = f1.readline()
    if not line1:
        print '\nbreak for not line\n'
        break
    if 'lab' in line1:
        flag = '0'
        num = 1
        while True:
            line2 = f1.readline()
            line3 = f1.readline()
            if iter < DN:    # if not up to the defined iteration
                if ' NONSPEECH' in line2 and line3[0] == '.':
                    if flag == '0':
                        iter = iter + int(1)
#                        print iter
                        break
                    else:
                        f2.write(line2)
                        f2.write(line3)
                        break
                elif ' SPEECH' in line2 and line3[0] == '.':
                    f2.write(line2)
                    f2.write(line3)
                    break
                else:
                    if num == 1:
                        f2.write(line1)
                        num = num + 1
                    f2.write(line2)
                    f2.write(line3)
                    flag = '1'   #update flag  
            else:     # if up to the defined iteration, all segments are writed in the new file
                if num == 1:
                    f2.write(line1)
                    num = num + 1  
                f2.write(line2)
                f2.write(line3)
                if line3[0] == '.':
                    break 
f1.close
f2.close
