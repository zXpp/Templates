#!/usr/bin/python

#!/share/spandh.ami1/sw/std/python/v2.7.5/Python-2.7.5/python
# rosanna
# ------------------------------------------------
import sys

# ------------------------------------------------
def readmlf(fname, files):#, spkrs):
    f = open(fname,'r')
    curr_file = ""
    episode = ""
    file = []
    for l in f:
	line = l.strip()
	if ".lab" in line or ".rec" in line:
            episode = line[3:16]
	    if curr_file != episode:
		files.append([curr_file, file])
		curr_file = episode
		file = []
            
            start = float(line[20:26])/100.0
#            print line[26:33]
            end   = float(line[27:33])/100.00
#            print line[34:41]
            spkr = line[17:19]
            if end > start:
                rttmline = "SPEAKER\t%s\t1\t%.2f\t%.2f\t<NA>\t<NA>\t%s\t<NA>" % (episode, start, end-start, spkr)
    	        file.append(rttmline)
    files.append([curr_file, file])
    f.close()

# ------------------------------------------------
def printClass(files):#, spkrs):
    for fi in files:
	if fi[1] != []:
	    print fi[0]
	    f = open("./rttm/" + fi[0] + ".sys.rttm", 'w')
	    header = ";;This is an RTTM file. Each record contains 9 whitespace separated fields:\n;;1:type        2:file  3:chnl  4:tbe   5:tdur  6:ortho 7:subtype       8:spkrname      9:conf"
	    print >> f, header
	    spkrline = "SPKR-INFO\t%s\t1\t<NA>\t<NA>\t<NA>\tunknown\tspeaker\t<NA>" % (fi[0])
	    print >> f, spkrline
	    data = fi[1]
	    for i in data:
	    	print >> f, i
	    f.close()

# ------------------------------------------------
# MAIN
# ------------------------------------------------

print "------------------------------------------------"
print "USAGE: python scriptname.py filelist etc"
print "------------------------------------------------"

files = []
#spkrs = {}
readmlf(sys.argv[1], files)#, spkrs)
printClass(files)#, spkrs)

print "------------------------------------------------"
