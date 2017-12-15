#!/usr/bin/python
#if the endpoint of one segment is not equal to the startpoint of its succeeding
# segment, then force them to be equal.
import os,sys
filepath='/share/spandh.ami1/usr/yanxiong/tnet.amiIND+tbl12MIX-tbl40IND+tbl10MIX.sad/nn.368.1000.1000.2/test_hyp.mlf-prob0.85-sf0.4-mix10'
oldfile = filepath
f = open(oldfile,'r')
lastend = 0.0
iter = 1
while True:
    line = f.readline()
    if 'TBL' in line:
        iter = 1
    if 'SPEECH' in line:
        line1 = line.split()          
        if iter > 1:
            if lastend != float(line1[0]):
                print line1
                print "Error!!"
                print "Start point is: "
                print line1[0]
                print "End point is: "
                print line1[1]
                print "Last end point must be equal to start point!"
                sys.exit()
        if float(line1[1]) < float(line1[0]):
            print line1
            print "Error!!"
            print "Start point is: "
            print line1[0]
            print "End point is: "
            print line1[1]
            print "End point must be larger than start point!"
            sys.exit()
        lastend = float(line1[1])
        iter = iter + 1
#        print lastend 
#        print iter
    elif not line:
        break
f.close
