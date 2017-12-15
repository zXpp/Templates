# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:47:09 2016

@author: zzpp220
"""
#from pandas import Series
from pandas import DataFrame
brandnamelist=["Apple_iPhone5","HTC_Desire_c","HTC_Sensation_xe","LG_GS290","LG_L3","LG_Optimus_L5","LG_Optimus_L9","Nokia_5530","Nokia_C5","Nokia_N70","Samsung_E1230","Samsung_E2121B","Samsung_E2600","Samsung_Galaxy_GT-I9100_s2","Samsung_Galaxy_Nexus_S","Samsung_Gt-I8190_mini","Samsung_Gt-N7100","Samsung_S5830i","Sony_Ericson_c510i","Sony_Ericson_c902","Vodafone_joy_845"]
data={}
for ele in brandnamelist:
    data.setdefault(ele,0)
    data[ele]=range(0,21)
chart=DataFrame(data,index=brandnamelist)
print chart