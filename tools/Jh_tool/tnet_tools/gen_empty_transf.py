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
(options, args) = parser.parse_args()

if(len(sys.argv) == 1):
    parser.print_help()
    sys.exit()

dimIn = int(options.dimIn)
print '<expand>', dimIn, dimIn
print 'v 1 0'
