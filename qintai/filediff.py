# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016年11月24日

@function: find the diffrence of two files, display the newest info.
@author: Stering
'''

def readtxt(filename):
	thelist=[]
	f=open(filename)
	for line in f:
		if line.find('主题')!=-1:
			thelist.append(line)
	return thelist

def compfile(new, old):
	sold=set(old)
	snew=set(new)
	ret=list(snew.difference(sold))
	return ret

if __name__=='__main__':
	oldfile='performanceList.txt'
	newfile='temp.txt'

	old=readtxt(oldfile)
	new=readtxt(newfile)
	ret=compfile(new, old)
	for i in ret:
		print i