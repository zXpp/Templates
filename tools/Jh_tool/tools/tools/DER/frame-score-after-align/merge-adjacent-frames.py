#!/usr/bin/python
# this script is to merge many adjacent SPEECH lines into one
import os,sys
oldfile = sys.argv[1] 
newfile = oldfile + '.merged'
f = open(oldfile, 'r')
nf = open(newfile, 'wa')
nf.write('#!MLF!#\n')
lastspkr = ' '
lastend = '1000000000000'
iter = 1
while True:
    line1 = f.readline()
    if not line1:
        break
    line = line1.split()
    if '.lab' in line1 or '.rec' in line1:
        if iter != 1:
            nf.write(lastend + ' ' + lastspkr + '\n.\n') # complete last line
        nf.write(line1)
        lastspkr = ' '  # update lastspkr
        lastend = '1000000000000'
        iter = 1
    elif len(line) >= 3:  # more than 3 columns
        if line[2] == lastspkr:
            if line[0] != lastend:
                nf.write(lastend + ' ' + lastspkr + '\n') # complete last line
                nf.write(line[0] + ' ')  # start new line
            lastend = line[1]  # update lastend
        else:
            if iter == 1:
                nf.write(line[0] + ' ')  # start new line
                iter = iter + 1
            else:
                nf.write(lastend + ' ' + lastspkr + '\n') # complete last line
                nf.write(line[0] + ' ')  # start new line
            lastend = line[1]  # update lastend
            lastspkr = line[2]   # update last speaker
nf.write(lastend + ' ' + lastspkr + '\n.\n') # complete last line
f.close
nf.close
