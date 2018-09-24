# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        temp = []
        if n >= 0:
            while n:
                remainder = n % 2
                temp.append(remainder)
                n = n // 2
            return sum(temp)
        else:
            temp = [(n>>i & 1) for i in range(32)]
            return sum(temp)



if __name__ == '__main__':
    s = Solution()
    n = -1
    print(s.NumberOf1(n))