
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# -*- coding:utf-8 -*-


class Solution:
    # 运行时间：26ms
    # 占用内存：5736k
    def Power(self, base, exponent):
        # write code here
        return base**exponent

    #运行时间：26ms
    #占用内存：5732k
    def PowerII(self, base, exponent):
        # write code here
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result


if __name__ == '__main__':
    s = Solution()
    base = 0.8
    exponent = 9
    print(s.Power(base, exponent))