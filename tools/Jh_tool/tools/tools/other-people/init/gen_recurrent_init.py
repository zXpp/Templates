
# ./gen_mlp_init.py
# script generateing NN initialization for training with TNet
#   
# author: Karel Vesely
#

import math, random
import sys


from optparse import OptionParser

parser = OptionParser()
parser.add_option('--dim', dest='dim', help='d1:d2:d3 layer dimensions in the network')
parser.add_option('--gauss', dest='gauss', help='use gaussian noise for weights', action='store_true', default=False)
parser.add_option('--negbias', dest='negbias', help='use uniform [-4.1,-3.9] for bias (default all 0.0)', action='store_true', default=False)
(options, args) = parser.parse_args()

if(options.dim == None):
  parser.print_help()
  sys.exit(1)


dimStrL = options.dim.split(':')
dimL = []
for i in range(len(dimStrL)):
  dimL.append(int(dimStrL[i]))



for layer in range(len(dimL)-1):
  print '<recurrent>', dimL[layer+1], dimL[layer]
  print 'm', dimL[layer+1], dimL[layer]+dimL[layer+1]
  for row in range(dimL[layer+1]):
    for col in range(dimL[layer]+dimL[layer+1]):
      if(options.gauss):
        print 0.1*random.gauss(0.0,1.0),
      else:
        print random.random()/5.0-0.1, 
    print
  print 'v', dimL[layer+1]
  for idx in range(dimL[layer+1]):
    if(options.negbias):
      print random.random()/5.0-4.1,
    else:
      print '0.0',
  print





