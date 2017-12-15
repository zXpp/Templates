#!/usr/bin/python
# this script is to transform TextGrid file to RTTM file
import re
 
file_object = open('tmp.txt')
try:
	str = file_object.read()
finally:
	file_object.close()
result = re.findall("(\d+%) S\s+\d+ (\d+)K\s+(\d+)K",str)
f = open("test.csv","w")
print result
for line in result:
	f.write("%s,%s,%s\n"%(line[0],line[1],line[2]))
f.close()
