#!/usr/bin/python
# find in path all '.TextGrid' text, include subdirtory!
import os,sys,math
path = '/media/jinhai/00C6CA35C6CA2B2C/hahaha/cv'
textname = 'cv'#build mlf filename

file2 = path + '/%s.mlf' % textname
f2 = open(file2, 'wa')
f2.write('#!MLF!#\n')   # write the first line
for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.TextGrid':
              	filepath = os.path.join(dirpath, filename)
		
		#main opt
		filename = filename[0 : filename.rfind('.')]
		string = filename
		file1 = path + '/%s.TextGrid' % string
		#file2 = path + '/%s.mlf' % string
		f1 = open(file1, 'rb')
		#f2 = open(file2, 'wa')
		#f2.write('#!MLF!#\n')   # write the first line
		f2.write('"*/%s.lab"\n' % string) # write the second line
		iter = 0
		lastlabel =''
		while True:
		    line1 = f1.readline()
		    if not line1:
		        break
		    elif 'intervals [' in line1:
		        line2 = f1.readline()
		        line2_temp = line2.split()
		        sp = str(int(round(float(line2_temp[2]) * 10000000)))   # change start point
		        f2.write(sp) # write start point     
		        f2.write(' ')   # write a space
		        line3 = f1.readline()
		        line3_temp = line3.split()
		        ep = str(int(round(float(line3_temp[2]) * 10000000)))   # change end point
		        f2.write(ep) # write end point
		        f2.write(' ')   # write a space
		        line4 = f1.readline()
		        line4_temp = line4.split()
		        if 'NONSPEECH' in line4 and line4_temp[2] == '"NONSPEECH"':
		            iter = int(iter) + 1
		            f2.write('NONSPEECH\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'NONSPEECH'
		            else:
		                if lastlabel == 'NONSPEECH':
		                    print iter
		                    print 'ERROR1 !'
		            lastlabel = 'NONSPEECH'
		        elif 'SPEECH' in line4 and line4_temp[2] == '"SPEECH"':   
		            iter = int(iter) + 1
		            f2.write('SPEECH\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'SPEECH'
		            else:
		                if lastlabel == 'SPEECH':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'SPEECH' 
		        elif 'SILENCE' in line4 and line4_temp[2] == '"SILENCE"':   
		            iter = int(iter) + 1
		            f2.write('SILENCE\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'SILENCE'
		            else:
		                if lastlabel == 'SILENCE':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'SILENCE' 
		        elif 'SN' in line4 and line4_temp[2] == '"SN"':   
		            iter = int(iter) + 1
		            f2.write('SN\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'SN'
		            else:
		                if lastlabel == 'SN':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'SN' 
		        elif 'MUSIC' in line4 and line4_temp[2] == '"MUSIC"':   
		            iter = int(iter) + 1
		            f2.write('MUSIC\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'MUSIC'
		            else:
		                if lastlabel == 'MUSIC':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'MUSIC' 
		        elif 'BELL' in line4 and line4_temp[2] == '"BELL"':   
		            iter = int(iter) + 1
		            f2.write('BELL\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'BELL'
		            else:
		                if lastlabel == 'BELL':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'BELL' 
		        elif 'IN' in line4 and line4_temp[2] == '"IN"':   
		            iter = int(iter) + 1
		            f2.write('IN\n') # write label
		            if int(iter) == 1:
		                lastlabel = 'IN'
		            else:
		                if lastlabel == 'IN':
		                    print iter
		                    print 'ERROR2 !'
		            lastlabel = 'IN' 
		        else:
			     f2.write('SN\n') # leak label
		             print iter
		             print 'ERROR3 !'
		#             sys.exit()
		f2.write('.\n')   # write the last line
		f1.close
		f2.close

               	print("file:" + filepath)
               	input_file = open(filepath)
               	text = input_file.read()
               	input_file.close()
               
              	output_file = open( filepath, 'w')
               	output_file.write(text)
               	output_file.close()
#string = 'car3'
#path = '/home/jinhai/jh'
#file1 = path + '/%s.TextGrid' % string
#file2 = path + '/%s.mlf' % string
#f1 = open(file1, 'r')
#f2 = open(file2, 'wa')
#f2.write('#!MLF!#\n')   # write the first line
#f2.write('"*/%s.lab"\n' % string) # write the second line
#iter = 0
#lastlabel =''
#while True:
#    line1 = f1.readline()
#    if not line1:
#        break
#    elif 'intervals [' in line1:
#        line2 = f1.readline()
#        line2_temp = line2.split()
#        sp = str(int(round(float(line2_temp[2]) * 10000000)))   # change start point
#        f2.write(sp) # write start point     
#        f2.write(' ')   # write a space
#        line3 = f1.readline()
#        line3_temp = line3.split()
#        ep = str(int(round(float(line3_temp[2]) * 10000000)))   # change end point
#        f2.write(ep) # write end point
#        f2.write(' ')   # write a space
#        line4 = f1.readline()
#        line4_temp = line4.split()
#        if 'NONSPEECH' in line4 and line4_temp[2] == '"NONSPEECH"':
#            iter = int(iter) + 1
#            f2.write('NONSPEECH\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'NONSPEECH'
#            else:
#                if lastlabel == 'NONSPEECH':
#                    print iter
#                    print 'ERROR1 !'
#            lastlabel = 'NONSPEECH'
#        elif 'SPEECH' in line4 and line4_temp[2] == '"SPEECH"':   
#            iter = int(iter) + 1
#            f2.write('SPEECH\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'SPEECH'
#            else:
#                if lastlabel == 'SPEECH':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'SPEECH' 
#        elif 'SILENCE' in line4 and line4_temp[2] == '"SILENCE"':   
#            iter = int(iter) + 1
#            f2.write('SILENCE\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'SILENCE'
#            else:
#                if lastlabel == 'SILENCE':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'SILENCE' 
#        elif 'SN' in line4 and line4_temp[2] == '"SN"':   
#            iter = int(iter) + 1
#            f2.write('SN\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'SN'
#            else:
#                if lastlabel == 'SN':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'SN' 
#        elif 'MUSIC' in line4 and line4_temp[2] == '"MUSIC"':   
#            iter = int(iter) + 1
#            f2.write('MUSIC\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'MUSIC'
#            else:
#                if lastlabel == 'MUSIC':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'MUSIC' 
#        elif 'BELL' in line4 and line4_temp[2] == '"BELL"':   
#            iter = int(iter) + 1
#            f2.write('BELL\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'BELL'
#            else:
#                if lastlabel == 'BELL':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'BELL' 
#        elif 'IN' in line4 and line4_temp[2] == '"IN"':   
#            iter = int(iter) + 1
#            f2.write('IN\n') # write label
#            if int(iter) == 1:
#                lastlabel = 'IN'
#            else:
#                if lastlabel == 'IN':
#                    print iter
#                    print 'ERROR2 !'
#            lastlabel = 'IN' 
#        else:
#             print iter
#             print 'ERROR3 !'
##             sys.exit()
#f2.write('.\n')   # write the last line
#f1.close
#f2.close
