#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:39:36 2018

@author: vijaygao
"""

#从尾到头打印链表
#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # 思路就是如果listNode存在，那就把它加进test这里list里面，直到没有listNode为止。
        # 最后返回test的逆顺序。
        test = []
        while listNode:
            test.append(listNode.val)
            listNode = listNode.next
        return test[::-1]

if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print(s.printListFromTailToHead(node1))