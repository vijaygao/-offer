# -*- coding:utf-8 -*-
from typing import List, Any, Union


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        max_num = rotateArray[0]
        for i in range(len(rotateArray)):
            if rotateArray[i] < max_num:
                return rotateArray[i]
            max_num = rotateArray[i]
        return rotateArray[0]

if __name__ == '__main__':
    s = Solution()
    test = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print(s.minNumberInRotateArray(test))