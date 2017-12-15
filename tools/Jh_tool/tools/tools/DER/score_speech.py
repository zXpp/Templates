#!/usr/bin/python
#rosanna
# ------------------------------------------------
import os, sys, commands

# ------------------------------------------------
def convert(fname):
    f = open(fname, 'r')
    for l in f:
	x = l.strip()
	convert = "seg2rttm.py %s.seg > %s.rttm" % (x,x)
	commands.getoutput(convert)
    f.close()

# ------------------------------------------------
def score(fname):
    f = open(fname, 'r')
    num_files = 0
    for l in f:
        x = l.strip()
        score = "/share/spandh.ami1/usr/yanxiong/tools/DER/md-eval.pl -as -c 0.25 -r /share/spandh.ami1/dia/bbc/tbl/lib/TBL/reference/speech/%s.speech.ref.rttm -u /share/spandh.ami1/dia/bbc/tbl/lib/TBL/reference/uem/%s.uem -s ./rttm/%s.sys.rttm > ./der/%s.der" % (x,x,x,x)
	print score
        commands.getoutput(score)
    	num_files += 1
    f.close()
    return num_files

# ------------------------------------------------
def collect(fname, stats, num_files):
    f = open(fname, 'r')
    total_m_time = 0.0
    total_m_per = 0.0
    total_f_time = 0.0
    total_f_per = 0.0
    total_s_time = 0.0
    total_s_per = 0.0
    total_der_per = 0.0
    for l in f:
        x = l.strip()
        m_time = 0.0
        m_per = 0.0
        f_time = 0.0
        f_per = 0.0
        s_time = 0.0
        s_per = 0.0
        der_per = 0.0
	der = "./der/%s.der" % (x)
	d = open(der, 'r')
	for line in d:
	    y = line.split()
	    if "MISSED SPEAKER TIME =" in line:
		m_time = float(y[4])
		temp = y[7]
		if temp == "percent":
		    temp = y[6].replace("(","")
		m_per = float(temp)
            if "FALARM SPEAKER TIME =" in line:
                f_time = float(y[4])
                temp = y[7]
                if temp == "percent":
                    temp = y[6].replace("(","")
                f_per = float(temp)
            if " SPEAKER ERROR TIME =" in line:
                s_time = float(y[4])
                temp = y[7]
                if temp == "percent":
                    temp = y[6].replace("(","")
                s_per = float(temp)
	    if " OVERALL SPEAKER DIARIZATION ERROR =" in line:
		der_per = float(y[5])
	stats[x] = [m_time, m_per, f_time, f_per, s_time, s_per, der_per]
	total_m_time += m_time
        total_m_per += m_per
        total_f_time += f_time
        total_f_per += f_per
        total_s_time += s_time
        total_s_per += s_per
        total_der_per += der_per
    stats["TOTAL"] = [total_m_time/num_files, total_m_per/num_files, total_f_time/num_files, total_f_per/num_files, total_s_time/num_files, total_s_per/num_files, total_der_per/num_files]
    d.close()
    f.close()

# ------------------------------------------------
def findSpkrs(fname, spkrs):
    f = open(fname, 'r')
    for l in f:
	x = l.strip()
	spkrs[x] = {}
        sys_count = 0
	sys_seg_count = 0
    	ref_count = 0
	ref_seg_count = 0
	sys = open("./rttm/"+x+".sys.rttm",'r')
	for line in sys:
	    if "SPKR-INFO" in line:
		sys_count +=1
	    if "SPEAKER" in line:
		sys_seg_count += 1
	spkrs[x]["SYS"] = sys_count
        spkrs[x]["SYS_seg"] = sys_seg_count
        ref = open("/share/spandh.ami1/usr/yanxiong/data/tbl/speech.ref.rttm/"+x+".speech.ref.rttm",'r')
        for line in ref:
            if "SPKR-INFO" in line:
                ref_count +=1
	    if "SPEAKER" in line:
                ref_seg_count += 1
        spkrs[x]["REF"] = ref_count
	spkrs[x]["REF_seg"] = ref_seg_count
    f.close()
	


# ------------------------------------------------
def printClass(stats, spkrs):
    print "|| '''File''' || '''Missed time (pc)''' || '''Falarm time (pc)''' || '''Speaker error time (pc)''' || '''DER''' || '''REF speakers''' || '''SYS speakers''' || '''REF segments''' || '''SYS segments''' ||"
    for s in stats:
	li = stats[s]
	if s != "TOTAL":
	    print "|| %s || %.2f  (%.2f) || %.2f (%.2f) ||%.2f (%.2f) ||%.2f  || %d || %d || %d || %d ||" % (s, li[0], li[1], li[2], li[3], li[4], li[5], li[6], spkrs[s]["REF"], spkrs[s]["SYS"], spkrs[s]["REF_seg"], spkrs[s]["SYS_seg"])
	else:
	    print "|| '''%s''' || %.2f (%.2f) || %.2f (%.2f) || %.2f (%.2f) || %.2f ||" % (s, li[0], li[1], li[2], li[3], li[4], li[5], li[6])


# ------------------------------------------------
# MAIN
# ------------------------------------------------
#convert(sys.argv[1])
print sys.argv
print '\n'
num_files = score(sys.argv[1])
stats = {}
collect(sys.argv[1], stats, num_files)
spkrs = {}
findSpkrs(sys.argv[1],spkrs)
printClass(stats, spkrs)
