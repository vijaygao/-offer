# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表(m乘n)，需要返回列表
    def printMatrix1(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            # print(res,1)
            if matrix and matrix[0]:
                for row in matrix:
                    # print(row,2)
                    res.append(row.pop())
            # print(matrix,2.5)
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    # print(row,3)
                    res.append(row.pop(0))
        return res

    def printMatrix(self, matrix):
        # write code here
        result=[]
        while matrix:
            result=result+matrix.pop(0)
            if not matrix:
                break
            matrix=self.turn(matrix)
        return result

    def turn(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        B=[]
        for i in range(c):
            A=[]
            for j in range(r):
                A.append(matrix[j][i])
            B.append(A)
        B.reverse()
        return B

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    print(s.printMatrix(matrix))