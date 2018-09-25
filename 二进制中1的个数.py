# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 负数应该为绝对值原码，第一位变为1，然后取反(符号位不变)加1，这就是补码。
# 比如 -1。 000000000000001变1000000000001变1111111111111110变1111111111111111111

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
            temp = [(n >> i & 1) for i in range(32)]
            return sum(temp)


if __name__ == '__main__':
    s = Solution()
    n = -1
    print(s.NumberOf1(n))
    # number = int('11111111111111111111111111111111', 2)
    # print(number)
