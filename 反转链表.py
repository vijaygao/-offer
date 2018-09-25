# 输入一个链表，反转链表后，输出新链表的表头。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last


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
    last = s.ReverseList(node1)
    result = []
    while last:
        result.append(last.val)
        last = last.next
    print(result)