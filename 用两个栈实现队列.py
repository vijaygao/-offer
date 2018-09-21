# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()

if __name__ == '__main__':
    s = Solution()
    result = []
    s.push(1)
    s.push(2)
    result.append(s.pop())
    s.push(3)
    result.append(s.pop())
    result.append(s.pop())
    s.push(4)
    result.append(s.pop())
    s.push(5)
    result.append(s.pop())

    print(result)
