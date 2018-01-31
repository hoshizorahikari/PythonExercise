"""
剑指Offer 29：数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """使用字典"""
        dct = {}
        for i in numbers:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        n = len(numbers)
        for k, v in dct.items():
            if v > n / 2:
                return k
        return 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1, 2, 3, 2, 1, 2, 2]))
