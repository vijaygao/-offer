# -*- coding:utf-8 -*-
class Solution:
    # 传统递归过不去
    # def Fibonacci(self, n):
    #     # write code here
    #     if n == 0 or n == 1:
    #         return 1
    #     else:
    #         return self.Fibonacci(n-2) + self.Fibonacci(n-1)

    def Fibonacci(self, n):
        # write code here
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        if n >= 3:
            temp = [1, 1]
            for i in range(2, n):
                temp.append(temp[i-1]+temp[i-2])
            return temp[n-1]



if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.Fibonacci(n))