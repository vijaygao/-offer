# 输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        result = []
        while head:
            result.append(head.val)
            head = head.next
        if k > len(result) or k < 1:
            return
        return result[-k]

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
    k = 1
    print(s.FindKthToTail(node1, k))
