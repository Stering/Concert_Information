# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016年9月28日

@function: Get the performace list of qintai concert hall, and print into 
           a text file.
@author: Stering
'''
import urllib2, re

filename='temp.txt'


def get_info():
    str1=r'http://www.qtconcerthall.com/all_performance/'
    str2=r'/Show.showtime2/asc/all/all//'
    for i in range(1,50):
        bdurl=str1+str(i)+str2
        req=urllib2.Request(bdurl)
        response=urllib2.urlopen(req)
        html=response.read()
        if html.find('暂无演出信息')!=-1:
            break
        sear_cont(html)

def sear_cont(html):
    pat=re.compile(r'performanceListShowName')
    group=pat.split(html)
    for i in range(1, len(group)):
        content=group[i]
        detail={}
        pat=re.compile(r'/ticket/(\d+)">(.+?)</a>')
        match=pat.findall(content)
        detail['link']='\t链接：http://www.qtconcerthall.com/ticket/'+str(match[0][0])+'\n'
        detail['Title']='\t主题：'+ match[0][1] + '\n'
        
        pat=re.compile(r'<span>(.+?)<br')
        match=pat.findall(content)
        try:   
            detail['price']='\t票价：' + match[0] + '\n'
        except IndexError:
            detail['price']='\t票价：None\n'
        
        pat=re.compile(r'<br />(.+?)&nbsp;(.+?)</span>')
        match=pat.findall(content)
        try:
            detail['date']='\t时间：' + match[0][0] + '\n'
            detail['addr']='\t地点：' + match[0][1] + '\n'
        except IndexError:
            pat=re.compile(r'<span>(.+?)&nbsp;(.+?)</span>')
            match=pat.findall(content)
            detail['date']='\t时间：' + match[0][0] + '\n'
            detail['addr']='\t地点：' + match[0][1] + '\n'
        info.append(detail)
#         output(detail, len(info))
    
def printInfo():
    f=open(filename, 'a+')
    f.write('总计：' + str(len(info)) + ' 场 \n')
    for i in range(len(info)):
        f.write(str(i+1) + ':\n')
        f.write(info[i]['Title'])
        f.write(info[i]['price'])
        f.write(info[i]['date'])
        f.write(info[i]['addr'])
        f.write(info[i]['link'])
    f.close()
        
if __name__=='__main__':
    f=open(filename, 'w+')
    f.write('琴台音乐厅音乐会：\n')
    f.close()
    info=[]
    get_info()
    printInfo()