# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here
#         listHead = ListNode(0)
#         start = listHead
#         while pHead1 and pHead2:
#             if pHead1.val <= pHead2.val:
#                 listHead.next = pHead1
#                 pHead1 = pHead1.next
#             else:
#                 listHead.next = pHead2
#                 pHead2 = pHead2.next
#             listHead = listHead.next
#         if pHead1:
#             listHead.next = pHead1
#         elif pHead2:
#             listHead.next = pHead2
#         return start.next
#
#     def Merge1(self, pHead1, pHead2):
#         listHead = None
#         if not pHead1 and not pHead2:
#             return
#         elif not pHead1:
#             return pHead2
#         elif not pHead2:
#             return pHead1
#         elif pHead1.val <= pHead2.val:
#             listHead = pHead1
#             listHead.next = self.Merge1(pHead1.next, pHead2)
#         else:
#             listHead = pHead2
#             listHead.next = self.Merge1(pHead1, pHead2.next)
#         return listHead
#
#
# if __name__ == '__main__':
#     s = Solution()
#     pHead1 = ListNode(1)
#     node1 = ListNode(3)
#     node2 = ListNode(5)
#     pHead2 = ListNode(2)
#     node3 = ListNode(4)
#     node4 = ListNode(6)
#     pHead1.next = node1
#     node1.next = node2
#     pHead2.next = node3
#     node3.next = node4
#     last = s.Merge1(pHead1, pHead2)
#     result = []
#     while last:
#         result.append(last.val)
#         last = last.next
#     print(result)


def merge(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1[0])
            del list1[0]
        else:
            result.append(list2[0])
            del list2[0]
    if list1:
        result.extend(list1)
    if list2:
        result.extend(list2)
    return result

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = merge(list1, list2)
for i in range(len(result)):
    if i != len(result) - 1:
        print(result[i], end=' ')
    else:
        print(result[i])

