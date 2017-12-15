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
	x = l.split()
	if ".lab" in line:
            episode = line.replace("\"*/", "")
	    episode = episode.replace(".lab\"", "")
	    if curr_file != episode:
		files.append([curr_file, file])
		curr_file = episode
		file = []
	if len(x) == 3:
	    
	    if x[2] != "NONSPEECH":	    
            	start = float(x[0])/10000000.0
                end   = float(x[1])/10000000.00
            	#end = float(x[1].replace(".lab\"", ""))/10000000.00
            	rttmline = "SPEAKER\t%s\t1\t%f\t%f\t<NA>\t<NA>\tspeech\t<NA>" % (episode, start, end-start)
	    	file.append(rttmline)
    files.append([curr_file, file])
    f.close()

# ------------------------------------------------
def printClass(files):#, spkrs):
    for fi in files:
	if fi[1] != []:
	    print fi[0]
	    f = open("./rttm/" + fi[0] + ".speech.ref.rttm", 'w')
	    header = ";;This is an RTTM file. Each record contains 9 whitespace separated fields:\n;;1:type        2:file  3:chnl  4:tbe   5:tdur  6:ortho 7:subtype       8:spkrname      9:conf"
	    print >> f, header
	    spkrline = "SPKR-INFO\t%s\t1\t<NA>\t<NA>\t<NA>\tunknown\tspeech\t<NA>" % (fi[0])
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
