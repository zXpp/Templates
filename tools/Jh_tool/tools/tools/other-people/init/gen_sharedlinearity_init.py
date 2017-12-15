
# ./gen_hamm_dct.py
# script generateing NN initialization for training with TNet
#   
# author: Karel Vesely

# calling example:
# python gen_mlp_init.py --dimIn=598 --dimOut=135 --dimHid=1024:1024:1024 
#

import math, random
import sys


from optparse import OptionParser

parser = OptionParser()
parser.add_option('--dim', dest='dim', help='d1:d2:d3 layer dimensions in the network')
parser.add_option('--inst', dest='inst', help='i1:i2 number of weight instances per layer')
parser.add_option('--gauss', dest='gauss', help='use gaussian noise for weights', action='store_true', default=False)
parser.add_option('--negbias', dest='negbias', help='use uniform [-4.1,-3.9] for bias (default all 0.0)', action='store_true', default=False)
parser.add_option('--linBNdim', dest='linBNdim', help='dim of linear bottleneck (sigmoids will be omitted, bias will be zero)',default=0)

(options, args) = parser.parse_args()

if(options.dim == None):
    parser.print_help()
    sys.exit(1)


dimStrL = options.dim.split(':')
dimL = []
for i in range(len(dimStrL)):
    dimL.append(int(dimStrL[i]))


instStrL = options.inst.split(':')
instL = []
for i in range(len(instStrL)):
    instL.append(int(instStrL[i]))

#check the divisibility
assert(len(dimL) == len(instL)+1)
for i in range(len(instL)):
    assert(dimL[i] % instL[i] == 0)
    assert(dimL[i+1] % instL[i] == 0)


for layer in range(len(dimL)-1):
    print '<sharedlinearity>', dimL[layer+1], dimL[layer]
    print instL[layer]
    print 'm', dimL[layer+1]/instL[layer], dimL[layer]/instL[layer]
    for row in range(dimL[layer+1]/instL[layer]):
        for col in range(dimL[layer]/instL[layer]):
            if(options.gauss):
                print 0.1*random.gauss(0.0,1.0),
            else:
                print random.random()/5.0-0.1, 
        print
    print 'v', dimL[layer+1]/instL[layer]
    for idx in range(dimL[layer+1]/instL[layer]):
        if(int(options.linBNdim) == dimL[layer+1]):
            print '0.0',
        elif(options.negbias):
            print random.random()/5.0-4.1,
        else:
            print '0.0',
    print
    if(int(options.linBNdim) != dimL[layer+1]):
       print '<sigmoid>', dimL[layer+1], dimL[layer+1]





