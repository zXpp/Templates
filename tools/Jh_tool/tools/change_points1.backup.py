#!/usr/bin/python
#if the endpoint of one segment is not equal to the startpoint of its succeeding
# segment, then force them to be equal.
import os,sys
oldfile = '/share/spandh.ami1/usr/yanxiong/tnet.ami.acf.sad/t.mlf'
newfile = '/share/spandh.ami1/usr/yanxiong/tnet.ami.acf.sad/t.mlf1'
f = open(oldfile,'r')
while True:
    line = f.readline()
    if 'SPEECH' in line:
        line = line.split()
        if int(line[1]) < int(line[0]):
            print line
            print "Error!!"
            print "Start point is: "
            print line[0]
            print "End point is: "
            print line[1]
            print "End point must be larger than start point!"
            sys.exit()
    elif not line:
        break
f.close

f = open(oldfile,'r') #open file again for changing discontinuous points
nf = open(newfile,'wa')
flag = 1 #indicate whether current line is the first line of LAB files
while True:
    line = f.readline()
    if 'SPEECH' in line:
        line = line.split()
        length = len(line) # component number of this line
        endtime = line[1]
        if flag == 1:
            nf.write(line[0])
            nf.write(' ')
            nf.write(line[1])
            nf.write(' ')
            nf.write(line[2])
            if length == 4:
                nf.write(' ')
                nf.write(line[3])
            nf.write('\n')
            flag = 2
        else:
            if lastendpoint != line[0]:
                nf.write(lastendpoint)
                nf.write(' ')
                nf.write(line[1])
                nf.write(' ')
                nf.write(line[2])
                if length == 4:
                    nf.write(' ')
                    nf.write(line[3])
                nf.write('\n')
            else:
                nf.write(line[0])
                nf.write(' ')
                nf.write(line[1])
                nf.write(' ')
                nf.write(line[2])
                if length == 4:
                    nf.write(' ')
                    nf.write(line[3])
                nf.write('\n')
        line = f.readline()
        if 'SPEECH' in line:
            line = line.split()
            length = len(line) # component number of this line 
            lastendpoint = line[1]
            if endtime != line[0]:
                nf.write(endtime)
                nf.write(' ')
                nf.write(line[1])
                nf.write(' ')
                nf.write(line[2])
                if length == 4:
                    nf.write(' ')
                    nf.write(line[3])
                nf.write('\n')
            else:
                nf.write(line[0])
                nf.write(' ')
                nf.write(line[1])
                nf.write(' ')
                nf.write(line[2])
                if length == 4:
                    nf.write(' ')
                    nf.write(line[3])
                nf.write('\n')
        else:
            if '*' in line:
                flag = 1 #indicate new LAB file begin
            nf.write(line)
    elif not line:
        break
    else:
        if '*' in line:
            flag = 1 #indicate new LAB file begin
        nf.write(line)
f.close
nf.close

