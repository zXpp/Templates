# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:44:49 2016

@author: zzpp220
"""
import re
raw = "Do you love Canglaoshi? Canglaoshi is a good teacher."
raw_list=raw.split(" ")

for i,ele in enumerate(raw_list):
    m=re.match(r'Canglaoshi(.?)',ele)
    if m:
        print ele
        ele='php'+m.group(1)
        raw_list[i]=ele
raw_new=" ".join(raw_list)
print raw_new