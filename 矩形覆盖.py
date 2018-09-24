# -*- coding:utf-8 -*-

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        if number >= 3:
            temp = [1, 2]
            for i in range(2, number):
                temp.append(temp[i-1]+temp[i-2])
            return temp[number-1]


if __name__ == '__main__':
    s = Solution()
    number = 4
    print(s.rectCover(number))