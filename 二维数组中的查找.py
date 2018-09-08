#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:49:19 2018

@author: vijaygao
"""
#343ms 5724k
def Find(target, array):
    # write code here
    i = len(array)-1
    if len(array[0]) == 0:
        return False
    while i >= 0:
        if array[i][0] > target:
            i = i - 1
        else:   #二分查找法
            low = 0
            high = len(array[i])-1
            while low <= high:
                mid = int((low+high)/2)
                if array[i][mid] > target:       
                    high = mid - 1
                elif array[i][mid] < target:
                    low = mid + 1
                else:
                    return True
            i = i - 1
    return False

#运行时间：222ms
#占用内存：5732k
def Find1(target,array):
    n = len(array)
    for i in range(n):
        if target in array[i]:
            return True
    return False


#运行时间：56ms
#占用内存：9644k
class Solution:
    # array 二维列表
    def Find2(self, target, array):
        # write code here
        n = len(array)
        flag = 'false'
        for i in range(n):
            if target in array[i]:
                flag = 'true'
                break
        return flag
    
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(input()))
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break


array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = 5
print(Find2(target, array))