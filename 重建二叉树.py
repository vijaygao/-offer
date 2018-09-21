# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    root = s.reConstructBinaryTree(pre, tin)
    result_pre = []
    result_mid = []
    result_after = []

    def preTraverse(root):  # 前序，中序，后序遍历其实是同一个function
        if root is None:
            return
        result_pre.append(root.val)
        preTraverse(root.left)
        result_mid.append(root.val)
        preTraverse(root.right)
        result_after.append(root.val)
    preTraverse(root)

    print(result_pre)
    print(result_mid)
    print(result_after)
