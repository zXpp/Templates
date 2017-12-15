#!/usr/bin/python
# this script can only transform ONE file contained in RTTM to TextGrid file

import os,sys,math

if len(sys.argv) != 2:
   print "\n USAGE: scriptname RTTMfile"
   sys.exit()

file1 = sys.argv[1]
file2 = file1
while '/' in file2:
    file2 = file2[file2.find('/')+1 : len(file2)]  # delete '/'
file2 = file2[0 : file2.find('.')]

file2 = './' + file2 + '.TextGrid'

f1 = open(file1,'r')
f2 = open(file2,'wa')

###################################################################
# write the first 14 lines into TextGrid file, number of segments and total duration are unkonw and 
# thus they are inialized as random numbers
xmax = 1  # random number
n = 0  # random number
f2.write('File type = "ooTextFile"\n')   # write the first line
f2.write('Object class = "TextGrid"\n') # write the second line
f2.write('\n')  #write the third line
f2.write('xmin = 0\n')
f2.write('xmax = %f\n' % xmax)
f2.write('tiers? <exists>\n')
f2.write('size = 1\n')
f2.write('item []:\n')
f2.write('    item [1]:\n')
f2.write('        class = "IntervalTier"\n')
f2.write('        name = "speaker"\n')
f2.write('        xmin = 0\n')
f2.write('        xmax = %f\n' % xmax)
f2.write('        intervals: size = %d\n\n' % n)
###################################################################

###################################################################
# begin file conversion
f1 = open(file1,'r')
n = 0
xmax1 = 0  # endpoint of the first previous segments
xmax2 = 0 #  endpoint of the second previous segments
xmax3 = 0 #  endpoint of the third previous segments
xmax4 = 0 #  endpoint of the fourth previous segments
while True:
    line1 = f1.readline()
    if not line1:
        break
    elif '<NA>' in line1:
        templine = line1.split()
        if n == 0 and float(templine[3]) != 0.0:
            xmin = 0 
	    xmax = float(templine[3])
	    text = 'Nonspeech' # label
            n = n + 1
	    f2.write('        intervals [%d]:\n' % n)
            f2.write('            xmin = %f\n' % xmin)
            f2.write('            xmax = %f\n' % xmax)
	    f2.write('            text = "%s"\n' % text)
	    xmax1 = xmax            

	    xmin = float(templine[3])
            xmax = float(templine[3]) + float(templine[4])
            text = templine[7] # label
            n = n + 1
            f2.write('        intervals [%d]:\n' % n)
            f2.write('            xmin = %f\n' % xmin)
            f2.write('            xmax = %f\n' % xmax)
            f2.write('            text = "%s"\n' % text)
            xmax2 = xmax

	elif n == 0 and float(templine[3]) == 0.0:
	    xmin = float(templine[3])
            xmax = float(templine[3]) + float(templine[4])
	    text = templine[7] # label
            n = n + 1

            f2.write('        intervals [%d]:\n' % n)
            f2.write('            xmin = %f\n' % xmin)
            f2.write('            xmax = %f\n' % xmax)
            f2.write('            text = "%s"\n' % text)
	    xmax1 = xmax

	else:
# overlapped segments occur, endopoints of previous segments should be smaller than startpoint of current segment
# for inserting one silent segment
            if n <= 1: # if 1 segment is converted
		xmax4 = xmax
		xmax3 = xmax
                xmax2 = xmax
                xmax1 = xmax
            elif n <= 2 and n > 1: # if 2 segments are converted
                xmax4 = xmax1
                xmax3 = xmax1
                xmax2 = xmax1
                xmax1 = xmax
            elif n <= 3 and n > 2: # if 3 segments are converted
                xmax4 = xmax2
                xmax3 = xmax2
                xmax2 = xmax1
                xmax1 = xmax
            elif n > 3: # if 4 segments are converted
                xmax4 = xmax3
                xmax3 = xmax2
                xmax2 = xmax1
                xmax1 = xmax

	    cond1 = float(str(xmax4)) < float(str(templine[3])) and float(str(xmax3)) < float(str(templine[3]))
            cond2 = float(str(xmax2)) < float(str(templine[3])) and float(str(xmax1)) < float(str(templine[3]))
            cond3 = float(str(templine[3])) > float(str(xmax))  # endpoint larger than startpoint for silence
            if cond1 and cond2 and cond3:  # endpoints of 4 previous segments are smaller than startpoint of current segment, insert 1 silence
	    	xmin = max([xmax1, xmax2, xmax3, xmax4]) # endpoint of previous segment as startpoint of silence
            	xmax = float(templine[3]) # startpoint of current segment as endpoint of silence
            	text = 'Nonspeech' # label
            	n = n + 1
	        f2.write('        intervals [%d]:\n' % n)
        	f2.write('            xmin = %f\n' % xmin)
	        f2.write('            xmax = %f\n' % xmax)
        	f2.write('            text = "%s"\n' % text)

	    xmin = float(templine[3])
            xmax = float(templine[3]) + float(templine[4])
            text = templine[7] # label
            n = n + 1
            f2.write('        intervals [%d]:\n' % n)
            f2.write('            xmin = %f\n' % xmin)
            f2.write('            xmax = %f\n' % xmax)
            f2.write('            text = "%s"\n' % text)
f1.close
f2.close

##################################################################
# determine total number of segments and duration
# open f2 again for updating the first 14 lines
f2 = open(file2,'r+')
f2.write('File type = "ooTextFile"\n')   # write the first line
f2.write('Object class = "TextGrid"\n') # write the second line
f2.write('\n')  #write the third line
f2.write('xmin = 0\n')
f2.write('xmax = %f\n' % xmax)
f2.write('tiers? <exists>\n')
f2.write('size = 1\n')
f2.write('item []:\n')
f2.write('    item [1]:\n')
f2.write('        class = "IntervalTier"\n')
f2.write('        name = "speaker"\n')
f2.write('        xmin = 0\n')
f2.write('        xmax = %f\n' % xmax)
f2.write('        intervals: size = %d\n' % n)
f2.close

