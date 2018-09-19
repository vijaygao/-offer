#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:26:45 2018

@author: vijaygao
"""

#替换空格


#运行时间：21ms
#占用内存：5728k
def replaceSpace(s):
    # write code here
    s = s.replace(' ','%20')
    return s
    
'''
运行时间：20ms
占用内存：5856k
'''    
def replaceSpace1(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)
    
    
    
s = 'We Are Happy.'
print(replaceSpace1(s))