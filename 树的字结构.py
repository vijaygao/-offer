# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) \
               or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)

class Solution1:
    def __init__(self):
        self.lst = []

    def add_to_lst(self, pRoot):
        if pRoot is None:
            return
        self.lst.append(pRoot.val)
        self.add_to_lst(pRoot.left)
        self.add_to_lst(pRoot.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False

        self.add_to_lst(pRoot1)
        list1 = self.lst
        self.lst = []
        self.add_to_lst(pRoot2)
        list2 = self.lst
        while len(list1) != len(list2):
            if list1[:len(list2)] == list2:
                return True
            else:
                list1 = list1[1:]
        if list1 == list2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    print(s.HasSubtree(node1, node3))

