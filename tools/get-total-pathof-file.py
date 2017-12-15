# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:58:15 2016

@author: zzpp220
"""

import os,sys


def zx_absfpathtof(pathin,pathout=''):
	'''this func is to get the full files abspath and output to a file,score use this script to generate refer file
	'''
#path=r'/media/zzpp220/Data/Linux_Documents/Mobile/ILP/audio/train/wav'
	pathout=pathin if pathout in [' ','',None] else pathout
	listname=os.path.join(pathout,'files_list.list')
	with open(listname,'w',0) as fileinfo:
		for root,dirs,files in os.walk(pathin):
			for label in files:
				if 'files_list.list' not in label:
					fileinfo.write(os.path.join(root,label) + '\n')
				#fileinfo.write(label+'='+os.path.join(root,label) + '\n')

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print ("------------------------------------------------")
		print ("\nUSAGE: python  pyscript.py pathin pathout")
		print("\npathin:the path u want to know,pathout:where to put the output file_list")
		print ("\n---------- Error!! --------------------------------------")
		sys.exit()
	path,pout=sys.argv[1],sys.argv[2]
	zx_absfpathtof(path,pout)
