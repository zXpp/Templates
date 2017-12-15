#!/usr/bin/python
#
import os,sys,math
#str = '0101'
#file1 = '/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.asrsns/nn.368.1000.1000.1000.2/test_hyp.mlf.%s.hmm30' % str
#file2 = '/share/spandh.ami1/dia/mtg.ihm/exp/acftrain1sad1.ihm/dnn/base.asrsns/nn.368.1000.1000.1000.2/TBL%s-MIXA1_hyp.TextGrid' % str
string = 'test_1'
path = '/home/jinhai/tnet.meetings/nn.368.500.4'
file1 = path + '/%s.rec' % string
file2 = path + '/%s.TextGRid' % string

f1 = open(file1,'r')
f2 = open(file2,'wa')
f2.write('File type = "ooTextFile"\n')   # write the first line
f2.write('Object class = "TextGrid"\n') # write the second line
f2.write('\n')  #write the third line

# get xmax and interals size
n = 0
while True:
    line1 = f1.readline()    
    if not line1:
        break
    elif line1[0] == '.' and 'SPEECH' not in line1:
        templine = lastline.split()
        xmax = float(templine[1]) / 10000000  # change from ns to seconds
    lastline = line1    
    n = int(n) + 1 
f1.close

SegNum = int(n) - 3 # total number of segments
print 'total number of segments: '
print SegNum

f2.write('xmin = 0\n') 
f2.write('xmax = %f\n' % xmax)
f2.write('tiers? <exists>\n')
f2.write('size = 1\n')
f2.write('item []:\n')
f2.write('    item [1]:\n')
f2.write('        class = "IntervalTier"\n')
f2.write('        name = "speech"\n')
f2.write('        xmin = 0\n')
f2.write('        xmax = %f\n' % xmax)
f2.write('        intervals: size = %d\n' % SegNum)

f1 = open(file1,'r')
line1 = f1.readline() #read the first line
line1 = f1.readline() #read the second line
for i in range(1, int(SegNum)+1):
    line1 = f1.readline() # read a line
    line = line1.split()
    xmin = float(line[0]) / 10000000 # change from ns to second
    xmax = float(line[1]) / 10000000 # change from ns to second
    text = line[2] # label

    f2.write('        intervals [%d]:\n' % i)
    f2.write('            xmin = %f\n' % xmin)
    f2.write('            xmax = %f\n' % xmax)
    f2.write('            text = "%s"\n' % text)

f1.close
f2.close
