# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016年11月25日

@function: Get the details of a concert performance.
@author: Stering
'''

import urllib2, re

def getdetail(durl):
    req=urllib2.Request(durl)
    response=urllib2.urlopen(req)
    html=response.read()

    pat=re.compile(r'<div class="showTitle">演出介绍</div>')
    group=pat.split(html)
    pat=re.compile(r'<span style="color: #ff6600; font-size: small;"><strong>')
    group=pat.split(group[1])
    pat=re.compile(r'<p>&nbsp;</p>')
    group=pat.split(group[1])
    print group[0] # 多个网页规律太不一致，待继续


if __name__=='__main__':
	getdetail('http://www.qtconcerthall.com/ticket/1547')