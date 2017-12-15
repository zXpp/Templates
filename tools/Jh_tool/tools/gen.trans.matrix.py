#!/usr/bin/python
#
import os,sys
sn = 150  # number of states
i = 1
f = open("./trans.matrix.sh", "aw")
while i <= sn:
    j = 1
    f.write('       ')
    if i == 1:
        while j <= sn:
            if j == 2:
                f.write('1   ')
            else:
                f.write('0   ')
            j +=1
    elif i == sn:
        while j <= sn:
            f.write('0   ')
            j +=1
    else:
        while j <= sn:
            if j == i or j == i + 1:
                f.write('0.5 ')
            else:
                f.write('0   ')
            j +=1
    f.write('\n')
    i +=1
f.write('    <EndHMM>" >> $hmmdefs_file\n')
f.write('done')
f.close
