#!/share/spandh.ami1/sw/std/python/v2.7.5/Python-2.7.5/python
#rosanna
# ------------------------------------------------
import os, sys, commands

# ------------------------------------------------
def findfiles(fname):
    files = []
    f = open(fname,'r')
    for l in f:
        x = l.strip()
        files.append(x)
    f.close()
    return files

# ------------------------------------------------
def score(f, ref, uem, sys):
    der_score = "/share/spandh.ami1/sw/spl/sctk/v2.4.0/i386/bin/md-eval.pl -as -c 0.25 -r %s -u %s -s %s > output.der" % (ref, uem, sys)
    commands.getoutput(der_score)
    miss = 0.0
    miss_per = 0.0
    falarm = 0.0
    falarm_per = 0.0
    spkrerr = 0.0
    spkrerr_per = 0.0
    der_per = 0.0
    fin = open("output.der", 'r')
    for line in fin:
        y = line.split()
        if "MISSED SPEAKER TIME =" in line:
            miss = float(y[4])
            temp = y[7]
            if temp == "percent":
                temp = y[6].replace("(","")
            miss_per = float(temp)
        if "FALARM SPEAKER TIME =" in line:
            falarm = float(y[4])
            temp = y[7]
            if temp == "percent":
                temp = y[6].replace("(","")
            falarm_per = float(temp)
        if " SPEAKER ERROR TIME =" in line:
            spkrerr = float(y[4])
            temp = y[7]
            if temp == "percent":
                temp = y[6].replace("(","")
            spkrerr_per = float(temp)
        if " OVERALL SPEAKER DIARIZATION ERROR =" in line:
            der_per = float(y[5])
    fin.close()
    commands.getoutput("rm output.der")
    return [f, miss, miss_per, falarm, falarm_per, spkrerr, spkrerr_per, der_per]

# ------------------------------------------------
def findspkrs(ref, sys, stat):
    ref_spkr = 0
    ref_segs = 0
    fref = open(ref,'r')
    for line in fref:
	if "SPKR-INFO" in line:
	    ref_spkr +=1
        if "SPEAKER" in line:
            ref_segs += 1
    fref.close()
    sys_spkr = 0
    sys_segs = 0
    fsys = open(sys,'r')
    for line in fsys:
        if "SPKR-INFO" in line:
            sys_spkr +=1
        if "SPEAKER" in line:
            sys_segs += 1
    fsys.close()
    stat.append( [ref_spkr, sys_spkr, ref_segs, sys_segs] ) 

# ------------------------------------------------
def getarrays(fname, ext):
    f = open(fname, 'r')
    flist = []
    for line in f:
        if "SPEAKER" in line:
            l = line.split()
            start = float(l[3])
            end = float(l[3]) + float(l[4])
            flist.append("%.2f" % start)
            flist.append("%.2f" % end)
    f.close()
    f = open("temp"+ext, 'w')
    old = ""
    for boundary in flist:
        if old != boundary:
            print >> f, boundary
        old = boundary
    f.close()
    return len(flist)

# ------------------------------------------------
def findboundary(ref, sys, stat):
    reflen = getarrays(ref, ".ref")
    syslen = getarrays(sys, ".sys")
    #output = commands.getoutput("matlab -r 'get_scores;exit;' > output")
    output = commands.getoutput("/share/spandh.ami1/sw/spl/octave/v3.6.3/x86_64/bin/octave '/share/spandh.ami1/usr/rosanna/dia_scoring/get_scores.m' > output")
    overall_score = 0
    nmatches = 0
    nins = 0
    ndel = 0
    fin = open("output", 'r')
    for line in fin:
  	l = line.split()
     	if "overall_score" in line:
	    overall_score = float(l[2])
	if "nmatches" in line:
	    nmatches = int(l[2])
	if "nins" in line:
	    nins = int(l[2])
	if "ndel" in line:
	    ndel = int(l[2])
    fin.close()
    commands.getoutput("rm output")
    nmatches_per = float(nmatches)/float(syslen)*100.0	# compared to system
    nins_per = float(nins)/float(syslen)*100.0		# compared to system
    ndel_per = ndel/float(reflen)*100.0			# compared to reference
    err_per = (nins_per + ndel_per) / float(reflen) * 100.0
    stat.append( [float(overall_score)/reflen, nmatches, float(nmatches)/float(syslen)*100.0, nins, float(nins)/float(syslen)*100.0, ndel, ndel/float(reflen)*100.0, err_per] )
    commands.getoutput("rm temp.ref")
    commands.getoutput("rm temp.sys")

# ------------------------------------------------
def findtotal(stats, num_files):
    miss = 0.0
    miss_per = 0.0
    falarm = 0.0
    falarm_per = 0.0
    spkrerr = 0.0
    spkrerr_per = 0.0
    der_per = 0.0
    overall_score = 0.0
    nmatches = 0.0
    nmatches_per = 0.0
    nins = 0.0
    nins_per = 0.0
    ndel = 0.0
    ndel_per = 0.0
    err_per = 0.0
    for stat in stats:
        miss += stat[1]
	miss_per += stat[2]
    	falarm += stat[3]
    	falarm_per += stat[4]
    	spkrerr += stat[5]
    	spkrerr_per += stat[6]
    	der_per += stat[7]
    	overall_score += stat[9][0]
    	nmatches += stat[9][1]
   	nmatches_per += stat[9][2]
    	nins += stat[9][3]
  	nins_per += stat[9][4]
    	ndel += stat[9][5]
 	ndel_per += stat[9][6]
	err_per += stat[9][7]
    return ["'''AVG'''", miss/num_files, miss_per/num_files, falarm/num_files, falarm_per/num_files, spkrerr/num_files, spkrerr_per/num_files, der_per/num_files, overall_score/num_files, nmatches/num_files, nmatches_per/num_files, nins/num_files, nins_per/num_files, ndel/num_files, ndel_per/num_files, err_per/num_files]

# ------------------------------------------------
def printstats(stats, total):
    print "|| '''File''' || '''Miss (%)''' || '''Falarm (%)''' || '''Spkrerr (%)''' || '''DER %''' || || '''Rspkrs''' || '''Sspkrs''' || '''Rsegs''' || '''Ssegs''' || || '''DPcost ms''' || '''Nmatches (%)''' || '''Nins (%)''' || '''Ndels (%)''' || '''ERR %'''||"
    for stat in stats:
        print "|| %s || %.2f (%.2f) || %.2f (%.2f) || %.2f (%.2f) || %.2f || || %d || %d || %d || %d || || %s || %s (%.2f) || %s (%.2f) || %s (%.2f) || %.2f ||" % (stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], stat[6], stat[7], stat[8][0], stat[8][1], stat[8][2], stat[8][3], stat[9][0], stat[9][1], stat[9][2], stat[9][3], stat[9][4], stat[9][5], stat[9][6], stat[9][7])
    print "|| %s || %.2f (%.2f) || %.2f (%.2f) || %.2f (%.2f) || %.2f || || || || || || || %.2f || %d (%.2f) || %d (%.2f) || %d (%.2f) || %.2f ||" % (total[0], total[1], total[2], total[3], total[4], total[5], total[6], total[7], total[8], total[9], total[10], total[11], total[12], total[13], total[14], total[15])


# ------------------------------------------------
# MAIN
# ------------------------------------------------
print "------------------------------------------------"
print "USAGE: python score.py -rl /path/to/referencelist/file -sp /path/to/sysrttm/folder/ (--speech)"
print "------------------------------------------------"

if "-rl" in sys.argv:
    ind = sys.argv.index("-rl")
    reflist = sys.argv[ind+1]
else:
    print "***ERROR, no reference list defined."
if "-sp" in sys.argv:
    ind = sys.argv.index("-sp")
    syspath = sys.argv[ind+1]
else:
    print "***ERROR, no system path defined."
speech = ""
if "--speech" in sys.argv:
    speech = "on"
    print "***No speaker scoring selected."

files = findfiles(reflist)
stats = []
for f in files:
    print f
    if speech == "on":
        ref = "/share/spandh.ami1/dia/bbc/tbl/lib/TBL/reference/speech/%s.speech.ref.rttm" % f
    else:
    	ref = "/share/spandh.ami1/dia/bbc/tbl/lib/TBL/reference/%s.ref.rttm" % f
    uem = "/share/spandh.ami1/dia/bbc/tbl/lib/TBL/reference/uem/%s.uem" % f
    sys = syspath + "/" + f + ".sys.rttm"
    stat = score(f, ref, uem, sys)
    findspkrs(ref, sys, stat)
    findboundary(ref, sys, stat)
    stats.append(stat)
    #break
total = findtotal(stats, len(files))
printstats(stats, total)
print "------------------------------------------------"
