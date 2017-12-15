#!/usr/bin/python
# template

#import os,sys
from pyh import *
list=[(1,'Lucy',25),(2,'Tom',30),(3,'Lily',20)]
page = PyH('Test')
page<<div(style="text-align:center")<<h4('Test table')
mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
tr1 = mytab << tr(bgcolor="lightgrey")
tr1 << th('id') + th('name')+th('age')
for i in range(len(list)):
    tr2 = mytab << tr()
    for j in range(3):
        tr2 << td(list[i][j])
#==============================================================================
#         if list[i][j]=='Tom':
#             tr2.attributes['bgcolor']='yellow'
#         if list[i][j]=='Lily':
#             tr2[1].attributes['style']='color:red'
#==============================================================================
page.printOut('test.html')
