#!/usr/bin/python
# # This script is to generate scp lines according to one MLF file
#
import os,sys

#------------
def generate_channel_SCP(mlf, scp, channel_key, fea_path):
    StartPoint_B = 17 # start point of one segment begining at the 21th letter
    StartPoint_E = 23 # start point of one segment ending at the 27th letter
    EndPoint_B = 24   # end point of one segment begining at the 29th letter
    EndPoint_E = 30   #  end point of one segment ending at the 35th letter
    iter = 1 # number of Seg files
    mlf = open(mlf, 'r')
    scp = open(scp, 'wa')
    while True:
        line1 = mlf.readline() # read one line
        if not line1:
            break
        if '.lab' in line1 or '.rec' in line1:
            # extract startpoint of one segment
            startpoint = line1[StartPoint_B:StartPoint_E] # extract start point of one segment
            while True:
                if int(startpoint) == 0: # if startpoint equal to 0
                    startpoint = '0'
                    break
                elif startpoint[:1] == '0': # if the first letter is 0
                    startpoint = startpoint[1:len(startpoint)] # delete the first letter
                else:
                    break
            # extract endpoint of one segment
            endpoint = line1[EndPoint_B:EndPoint_E] # extract end point of one segment
            while True:
                if int(endpoint) == 0: # if endpoint equatl to 0
                    endpoint = '0'
                    break
                elif endpoint[:1] == '0': # if the first letter is 0
                    endpoint = endpoint[1:len(endpoint)] # delete the first letter
                else:
                    break
            segname = line1[3:30]
            filename = line1[3:11] + channel_key
            scp.write(segname + '.htk_post=')
            scp.write(fea_path + filename + '.htk_post[')
            scp.write(startpoint + ',' + endpoint + ']\n')
    mlf.close
    scp.close            

#--------------------------------
# main

print "------------------------------------------------"
print "USAGE: python scriptname.py ref-dnnNumber align-dnnNumber"
print "E.g. : python scriptname.py ref-dnn1 align-dnn1"
print "------------------------------------------------"

mlf_path = '/share/spandh.ami1/usr/yanxiong/SLT2014/mlf.ForAlign/';
scp_path = '/share/spandh.ami1/usr/yanxiong/SLT2014/scp.ForAlign/'
fea_path = '/share/spandh.ami1/usr/yanxiong/'
if sys.argv[1] == 'ref-dnn1':
    mlf = mlf_path + 'mlf.dnn1/test_hyp.mlf.dnn1.MIX.ForAlign'
elif sys.argv[1] == 'ref-dnn3':
    mlf = mlf_path + 'mlf.dnn3/test_hyp.mlf.dnn3.MIX.ForAlign'
elif sys.argv[1] == 'ref-dnn5':
    mlf = mlf_path + 'mlf.dnn5/test_hyp.mlf.dnn5.MIX.ForAlign'
elif sys.argv[1] == 'ref-dnn6':
    mlf = mlf_path + 'mlf.dnn6/test_hyp.mlf.dnn6.MIX.ForAlign'
else:
    print "ERROR! please enter ref-dnnNumber, e.g. ref-dnn1\n"
    sys.exit()

if sys.argv[2] == 'align-dnn1':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn1.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.ami-tbl.sad/onlyfbank/nn.368.1000.1000.2/fx/posteriors/'
elif sys.argv[2] == 'align-dnn2':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn2.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.ami-tbl.sad/fbank_auxfea/nn.480.1000.1000.2/fx/posteriors/'
elif sys.argv[2] == 'align-dnn3':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn3.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.amiIND+tbl48IND-tbl40IND.sad/onlyfbank/nn.368.1000.1000.2/fx/posteriors/'
elif sys.argv[2] == 'align-dnn4':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn4.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.amiIND+tbl48IND-tbl40IND.sad/fbank_auxfea/nn.480.1000.1000.2/fx/posteriors/'
elif sys.argv[2] == 'align-dnn5':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn5.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.amiIND+tbl12MIX-tbl40IND+tbl10MIX.sad/nn.368.1000.1000.2/fx/posteriors/'
elif sys.argv[2] == 'align-dnn6':
    scpfile = scp_path + 'scp.%s.%s/test_hyp.scp.dnn6.' % (sys.argv[1], sys.argv[2])
    fea_path =  fea_path + 'tnet.amiIND+tbl48IND+tbl12MIX-tbl40IND+tbl10MIX.sad/nn.368.1000.1000.2/fx/posteriors/'
else:
    print "ERROR! please enter align-dnnNumber, e.g. align-dnn1\n"
    sys.exit()

iter = 1
while True:    
    if iter == 1:
        channel_key = 'CAM01'
        scp = scpfile + channel_key + '.ForAlign' # scp file
        iter = iter + 1
    elif iter == 2:
        channel_key = 'CAM02'
        scp = scpfile + channel_key + '.ForAlign' # scp file
        iter = iter + 1
    elif iter == 3:
        channel_key = 'CAM12'
        scp = scpfile + channel_key + '.ForAlign' # scp file
        iter = iter + 1
    elif iter == 4:
        channel_key = 'CAM22'
        scp = scpfile + channel_key + '.ForAlign' # scp file
        iter = iter + 1
    else:
        break 
    # generate a scp file of an individual channel according to mix channel mlf
    generate_channel_SCP(mlf, scp, channel_key, fea_path) 
