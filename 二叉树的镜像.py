# 作给定的二叉树，将其变换为源二叉树的镜像。
# -*- coding:utf-8 -*-  {8,6,10,5,7,9,11}
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root != None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)


if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    s.Mirror(node1)
    print(node1.left.val)
    print(node1.right.val)