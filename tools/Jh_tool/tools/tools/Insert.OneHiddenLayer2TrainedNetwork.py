#!/usr/bin/python
# yanxiong
# this script is to insert one hidden layer of new initialized network to a trained network
# for layer by layer training
# ------------------------------------------------
import sys,os

if len(sys.argv) != 5:
    print "------------------------------------------------"
    print "\nUSAGE: python scriptname.py TrainedNetName NumOfHiddenLayerIntrainedNet NewInitNetName NumOfHiddenLayerInNewInitNet"
    print '\nTrainedNetName and NewInitNetName must be in the same folder! They must be file name instead of path!'
    print "\n---------- Error!! --------------------------------------"
    sys.exit()
TrainedNetName = sys.argv[1]
NumOfHiddenLayerIntrainedNet = sys.argv[2]
NewInitNetName = sys.argv[3]
NumOfHiddenLayerInNewInitNet = sys.argv[4]
if int(NumOfHiddenLayerIntrainedNet) != int(NumOfHiddenLayerInNewInitNet) - 1:
    print '\nNumber of hidden layer in trained net MUST be equal to Number of hidden layer in new initial net plus 1!\n'
    sys.exit()
f1 = open(TrainedNetName, 'r')
f2 = open(NewInitNetName, 'r')
f3 = open('./NewNetAfterInsertion', 'wa')
LayerCount1 = 0
LayerCount2 = 0
# read the first part of TrainedNetName and wirte in f3
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif 'biasedlinearity' in line1:
        LayerCount1 = LayerCount1 + 1
        if int(LayerCount1) > int(NumOfHiddenLayerIntrainedNet): # if this layer is beyond the NumOfHiddenLayerIntrainedNet-th hidden layer
            string1 = line1  # store this line for writing latter 
            break
        else:
            f3.write(line1)
    else:
        f3.write(line1)

# read the hidden layer parameters of NewInitNetName and wirte in f3
while True:
    line2 = f2.readline()
    if not line2:
        break
    elif 'biasedlinearity' in line2:
        LayerCount2 = LayerCount2 + 1
        if int(LayerCount2) == int(NumOfHiddenLayerInNewInitNet): # if this layer is the NumOfHiddenLayerInNewInitNet-th hidden layer
            f3.write(line2)
    else:
        if int(LayerCount2) == int(NumOfHiddenLayerInNewInitNet): # if this layer is still the NumOfHiddenLayerInNewInitNet-th hidden layer
            f3.write(line2)
        elif int(LayerCount2) == int(NumOfHiddenLayerInNewInitNet): # if this layer is beyond the NumOfHiddenLayerInNewInitNet-th hidden layer 
            break
f2.close

# read the second part of TrainedNetName and wirte in f3
f3.write(string1) # this line contains 'biasedlinearity'
while True:
    line1 = f1.readline()
    if not line1:
        break
    else:
        f3.write(line1)
f1.close
f3.close
