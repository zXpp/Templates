#!/usr/local/bin/python -u

# ./gen_hamm_dct.py
# script generateing input transform for NN training with TNet
#
# - context expansion, 
# - critical band transposition,
# - band-wise hamming window
# - DCT transform
#   
# author: Karel Vesely

from math import *


from optparse import OptionParser

import sys

parser = OptionParser()
parser.add_option('--dimIn', dest='dimIn', help='dimension of input features')
parser.add_option('--startFrmExt', dest='startFrmExt', help='frame count of left context')
parser.add_option('--endFrmExt', dest='endFrmExt', help='frame count of right context')
parser.add_option('--dctBaseCnt', dest='dctBaseCnt', help='nuber of dct bases')
(options, args) = parser.parse_args()

if(len(sys.argv) == 1):
    parser.print_help()
    sys.exit()

dimIn = int(options.dimIn)
startFrmExt = int(options.startFrmExt)
endFrmExt = int(options.endFrmExt)
dctBaseCnt = int(options.dctBaseCnt)


timeContext = (1+startFrmExt+endFrmExt)

# expand the time context
print '<expand>', dimIn*timeContext, dimIn
print 'v', timeContext
for idx in range(-startFrmExt,endFrmExt+1,1):
  print idx,
print '\n'

# 'transpose' the time windows
print '<transpose>', dimIn*timeContext, dimIn*timeContext
print timeContext, '\n'

# use hamming window
M_2PI = 6.283185307179586476925286766559005
print '<window>', dimIn*timeContext, dimIn*timeContext
print 'v', dimIn*timeContext
for band in range(dimIn):
  for i in range(timeContext):
    print str(0.54 - 0.46*cos((M_2PI * i) / (timeContext-1))),
  print 
print 

# dct transform
M_PI = 3.1415926535897932384626433832795
M_SQRT2 = 1.4142135623730950488016887
print '<blocklinearity>', dimIn*dctBaseCnt, dimIn*timeContext
print 'm', dctBaseCnt, timeContext
for k in range(dctBaseCnt):
  for n in range(timeContext):
    print str(sqrt(2.0/timeContext)*cos(M_PI/timeContext*k*(n+0.5))),
  print 
print 
 
