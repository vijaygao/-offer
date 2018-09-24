# -*- coding:utf-8 -*-
class Solution:
    # 每次最多跳一步，或者两部
    # def jumpFloor(self, number):
    #     # write code here
    #     if number == 0:
    #         return 0
    #     if number == 1:
    #         return 1
    #     if number == 2:
    #         return 2
    #     if number >= 3:
    #         temp = [1, 2]
    #         for i in range(2, number):
    #             temp.append(temp[i - 1] + temp[i - 2])
    #         return temp[number - 1]

    # 一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级
    def jumpFloorII(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        if number == 3:
            return 4
        if number >= 4:
            temp = [1, 2, 4]
            for i in range(3, number):
                value = 0
                for j in range(i):
                    value += temp[j]
                temp.append(value+1)
            return temp[number - 1]


if __name__ == '__main__':
    s = Solution()
    number = 4
    print(s.jumpFloorII(number))
