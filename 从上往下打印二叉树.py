# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
测试用例:
{10,6,14,4,8,12,16}
对应输出应该为:
[10,6,14,4,8,12,16]
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        l = []
        if not root:
            return []
        temp = [root]
        while len(temp):
            v = temp.pop(0)
            l.append(v.val)
            if v.left:
                temp.append(v.left)
            if v.right:
                temp.append(v.right)
        return l

if __name__ == '__main__':
    node = TreeNode(10)
    node1 = TreeNode(6)
    node2 = TreeNode(14)
    node3 = TreeNode(4)
    node4 = TreeNode(8)
    node5 = TreeNode(12)
    node6 = TreeNode(16)
    node.left = node1
    node.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    s = Solution()
    print(s.PrintFromTopToBottom(node))
