#!./python
#rosanna
# ------------------------------------------------
import os, sys, commands, os.path
import numpy as np

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
    der_score = "perl /home/winky/score/md-eval.pl -as -c 0.25 -r %s %s -s %s > %s.output.der" % (ref, uem, sys, sys)
    derlog = commands.getoutput(der_score)
    miss = 0.0
    miss_per = 0.0
    falarm = 0.0
    falarm_per = 0.0
    spkrerr = 0.0
    spkrerr_per = 0.0
    der_per = 0.0
    fin = open("%s.output.der" % sys, 'r')
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
    commands.getoutput("rm %s.output.der" % sys)
    return [f, miss_per, falarm_per, spkrerr_per, der_per]

# ------------------------------------------------
def findspkrs(ref, sys, stat):
    ref_spkr = []
    ref_segs = 0
    fref = open(ref,'r')
    for line in fref:
        if "SPEAKER" in line:
            ref_segs += 1
	    x = line.split()
	    if x[7] not in ref_spkr:
		ref_spkr.append(x[7])
    fref.close()
    sys_spkr = []
    sys_segs = 0
    fsys = open(sys,'r')
    for line in fsys:
        if "SPEAKER" in line:
            sys_segs += 1
	    x = line.split()
            if x[7] not in sys_spkr:
                sys_spkr.append(x[7])
    fsys.close()
    stat.append( [len(ref_spkr), len(sys_spkr), ref_segs, sys_segs] ) 

# ------------------------------------------------
def getarrays(fname, ext, sys):
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
    f = open(sys+".temp"+ext, 'w')
    old = ""
    for boundary in flist:
        if old != boundary:
            print >> f, boundary
        old = boundary
    f.close()
    return [len(flist), sys+".temp"+ext]

# ------------------------------------------------
def get_mscript(reflen, syslen):
  
	scriptinfo = "fid = fopen('%s', 'r');\nin = textscan(fid, '%s');\nfclose(fid);\nref = str2double(in{:});\n\n\nfid = fopen('%s', 'r');\nin = textscan(fid, '%s');\nfclose(fid);\nsys = str2double(in{:});\n\n\naddpath('/home/sisterqin/score/');\n[overall_score, nmatches, nins, ndel, ins_indices, del_indices, match_indices] = DP_boundary_alignment(sys,ref);\ndisp(['overall_score = ', num2str(overall_score)])\ndisp(['nmatches = ', num2str(nmatches)])\ndisp(['nins = ', num2str(nins)])\ndisp(['ndel = ', num2str(ndel)])" % ( reflen, "%s", syslen, "%s" )

	f = open(syslen+".m",'w')
	print >> f, scriptinfo
	f.close()
   	return syslen+".m"


# ------------------------------------------------
def findboundary(ref, sys, stat):
    [reflen, reftemp] = getarrays(ref, ".ref", sys)
    [syslen, systemp] = getarrays(sys, ".sys", sys)
    mscript = get_mscript(reftemp, systemp)
    output = commands.getoutput("/usr/local/MATLAB/R2014b/bin/glnxa64/MATLAB -nodesktop -nojvm -nosplash -nodisplay '%s' > %s.output" % (mscript, sys) )
    overall_score = 0
    nmatches = 0
    nins = 0
    ndel = 0
    fin = open("%s.output" % sys, 'r')
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
    commands.getoutput("rm %s.output" % sys)
    nmatches_per = float(nmatches)/float(reflen)*100.0	# compared to ref
    nins_per = float(nins)/float(reflen)*100.0		# compared to ref
    ndel_per = float(ndel)/float(reflen)*100.0		# compared to reference
    err_per = (nins_per + ndel_per) / 2 
    stat.append( [float(overall_score)/reflen, nmatches_per, nins_per, ndel_per, err_per] )

    #print [float(overall_score)/reflen, nmatches_per, nins_per, ndel_per, err_per]

    commands.getoutput("rm %s.temp.ref" % sys)
    commands.getoutput("rm %s.temp.sys" % sys)
    commands.getoutput("rm %s" % mscript)

# ------------------------------------------------
def puritymeasures(ref_name, sys_name):
    frames = {}
    clusters = {}
    spkrs = {}
    fref = open(ref_name, 'r')
    fsys = open(sys_name, 'r')
    end = 0
    for line in fref:
        if "SPEAKER" in line:
            x = line.split()
            spkr = x[7]
            start = int(float(x[3])*100.0)
            for j in range(end, start):
                frames[j] = {}
                frames[j]["r"] = ""
            dur = int(float(x[4])*100.0)
            end = start + dur
            for j in range(start, end):
                frames[j] = {}
                frames[j]["r"] = spkr
            if spkr not in spkrs:
                spkrs[spkr] = float(dur)
            else:
                spkrs[spkr] += float(dur)
    fref.close()
    fsys = open(sys_name, 'r')
    end = 0
    for line in fsys:
        if "SPEAKER" in line:
            x = line.split()
            spkr = x[7]
            start = int(float(x[3])*100.0)
            for i in range(end, start):
		if i not in frames:
			frames[i] = {}
                frames[i]["s"] = ""
            dur = int(float(x[4])*100.0)
            end = start + dur
            for i in range(start, end):
                if i not in frames:
                    frames[i] = {}
                frames[i]["s"] = spkr
            if spkr not in clusters:
                clusters[spkr] = float(dur)
            else:
                clusters[spkr] += float(dur)
    fsys.close()
    if i != j:
        diff = abs(i - j)
        if i < j:
            for n in range(0,diff):
                frames[i+n+1]["s"] = ""
	    new_len = i+n+1
        else:
            for n in range(0,diff):
                frames[j+1+n]["r"] = ""
	    new_len = j+1+n
	if new_len < len(frames):
		for i in range(new_len,len(frames)):
			if "r" not in frames[i]:
				frames[i]["r"] = ""
			if "s" not in frames[i]:
				frames[i]["s"] = ""
    N_s = float(len(spkrs))
    N_c = float(len(clusters))
    N = 0.0
    for f in frames:
        if frames[f]["r"] != "":
            N += 1
        elif frames[f]["s"] != "":
            N+=1
    acp,asp,k=0.0,0.0,0.0
    for c in clusters:
        p_i = 0.0
        for s in spkrs:
            n_ij = 0.0
            for f in frames:
	        if frames[f]["s"] == c:
                    if frames[f]["r"] == s:
                        n_ij += 1.0
            p_i += (n_ij ** 2.0) / (clusters[c] ** 2.0)
        acp += p_i * clusters[c]
    acp = acp / N
    for s in spkrs:
        p_j = 0.0
        for c in clusters:
            n_ij = 0.0
            for f in frames:
                if frames[f]["r"] == s:
                    if frames[f]["s"] == c:
                        n_ij += 1.0
            p_j += (n_ij ** 2.0) / (spkrs[s] ** 2.0)
        asp += p_j * spkrs[s]
    asp = asp / float(N)
    k = np.sqrt(acp*asp)
    return [acp*100.0, asp*100.0, k*100.0]


# ------------------------------------------------
def findtotal(stats, num_files, speech):
    miss_per = 0.0
    falarm_per = 0.0
    spkrerr_per = 0.0
    der_per = 0.0
    overall_score = 0.0
    nmatches_per = 0.0
    nins_per = 0.0
    ndel_per = 0.0
    err_per = 0.0
    acp = 0.0
    asp = 0.0
    k = 0.0
    num_ssegs = 0
    num_rsegs = 0
    for stat in stats:	
	miss_per += stat[1]
    	falarm_per += stat[2]
    	spkrerr_per += stat[3]
    	der_per += stat[4]
	num_rsegs += stat[5][2]
	num_ssegs += stat[5][3]
    	overall_score += stat[6][0]
   	nmatches_per += stat[6][1]
  	nins_per += stat[6][2]
 	ndel_per += stat[6][3]
	err_per += stat[6][4]
	acp += stat[7][0]
	asp += stat[7][1]
	k += stat[7][2]
    if speech == "yes":
	return ["'''AVG'''", miss_per/num_files, falarm_per/num_files, 0.0, (miss_per/num_files+falarm_per/num_files), num_rsegs, num_ssegs, overall_score/num_files, nmatches_per/num_files, nins_per/num_files, ndel_per/num_files, err_per/num_files, acp/num_files, asp/num_files, k/num_files]
    else:
	return ["'''AVG'''", miss_per/num_files, falarm_per/num_files, spkrerr_per/num_files, der_per/num_files, num_rsegs, num_ssegs, overall_score/num_files, nmatches_per/num_files, nins_per/num_files, ndel_per/num_files, err_per/num_files, acp/num_files, asp/num_files, k/num_files]

# ------------------------------------------------
def printstats(stats, total, mode, speech):
    	header =  "||File                      ||MS%||FA%||SE%||DER%|| ||Rspkr||Sspkr||Rseg||Sseg||"
    	if "-dp" in mode:
		header += " || '''DPcost ms''' || '''matches%''' || '''ins%''' || '''dels%''' || '''ERR%'''||"
	if "-pu" in mode:
		header += " ||ACP% ||ASP%||K% ||"
	print header
    	for stat in stats:
		if speech == "yes":
			line = "|| %s || %.2f\t || %.2f\t || %.2f\t || %.2f\t || || %d\t || %d\t || %d\t || %d\t ||" % (stat[0].split("/")[len(stat[0].split("/"))-1].split(".")[0], stat[1], stat[2],  0.0, stat[1]+stat[2],  stat[5][0], stat[5][1], stat[5][2], stat[5][3])
		else:
        		line = "|| %s || %.2f\t || %.2f\t || %.2f\t || %.2f\t || || %d\t || %d\t || %d\t || %d\t ||" % (stat[0].split("/")[len(stat[0].split("/"))-1].split(".")[0], stat[1], stat[2],  stat[3], stat[4],  stat[5][0], stat[5][1], stat[5][2], stat[5][3])
		if "-dp" in mode:
			line += " || %.2f\t || %.2f\t || %.2f\t || %.2f\t || %.2f\t ||" % (float(stat[6][0]), stat[6][1], stat[6][2], stat[6][3], stat[6][4])
		if "-pu" in mode:
			line += " || %.2f\t || %.2f\t || %.2f\t ||" % (stat[7][0], stat[7][1], stat[7][2])
		print line
    	if len(stats) > 1:
		line = "|| %s     || %.2f\t || %.2f\t || %.2f\t || %.2f\t || ||   \t ||   \t || %d || %d ||" % (total[0].split("/")[len(total[0].split("/"))-1], total[1], total[2], total[3], total[4], total[5], total[6])
		if "-dp" in mode:
			line += " || %.2f\t || %.2f\t || %.2f\t || %.2f\t || %.2f\t ||" % (total[7], total[8], total[9], total[10], total[11])
		if "-pu" in mode:
			line += " || %.2f\t || %.2f\t || %.2f\t ||" % (total[12], total[13], total[14])
		print line

# ------------------------------------------------
# MAIN
# ------------------------------------------------

mode = ""
if "-r" in sys.argv:
    	ind = sys.argv.index("-r")
    	reflist = sys.argv[ind+1]
else:
    	print "***ERROR, no reference list defined."
if "-s" in sys.argv:
    	ind = sys.argv.index("-s")
    	syspath = sys.argv[ind+1]
else:
    	print "***ERROR, no system path defined."

if "-u" in sys.argv:
	ind = sys.argv.index("-u")
	uempath = sys.argv[ind+1]
speech = "no"
if "--speech" in sys.argv:
	speech = "yes"


files = findfiles(reflist)
stats = []
num_files = 0
for f in files:
    fname = f.split("/")[len(f.split("/"))-1].replace(".ref.rttm","")
    print fname
    reff = "%s" % f
    sysf = syspath + "/" + fname + ".sys.rttm"
    if "-u" in sys.argv:
	uem = "-u " + uempath + "/" + fname + ".uem"
    else:
	uem = ""
    if os.path.isfile(sysf):
    	stat = score(f, reff, uem, sysf)
    	findspkrs(reff, sysf, stat)
	if "-dp" in sys.argv:
    		findboundary(reff, sysf, stat)
		mode += "-dp"
	else:
		stat.append([0,0,0,0,0])
	if "-pu" in sys.argv:
		stat.append( puritymeasures(reff, sysf) )
		mode += "-pu"
	else:
		stat.append([0,0,0])
    	stats.append(stat)
	num_files += 1

if num_files == 0:
	num_files = 1
total = findtotal(stats, num_files, speech)
printstats(stats, total, mode, speech)

print "------------------------------------------------"
