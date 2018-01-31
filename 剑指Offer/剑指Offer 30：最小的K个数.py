"""
剑指Offer 30：最小的K个数题目描述
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
from random import randint


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        return sorted(tinput)[0:k]


if __name__ == '__main__':
    arr = [randint(10, 99) for x in range(10)]
    print(Solution().GetLeastNumbers_Solution(arr, 3))
