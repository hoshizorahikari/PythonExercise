"""
75. 寻找峰值
一个整数数组(size为n)，具有以下特点：
相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
 注意事项：数组至少有一个峰值，数组可能含有多个峰值，返回任意一个，数组至少3个数字
样例：给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.
挑战：Time complexity O(logN)
标签：数组 LintCode 版权所有 二分法 谷歌
"""


class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak_1(self, A):
        # 顺序查找超时了...
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                return i

    def findPeak(self, A):
        # 峰值左边递增,右边递减,用二分查找
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid == 0:  # 能到此处说明start=0,end=1,且A[2]<A[1],又因为题中说A[0]>A[1],所以1肯定是峰值
                return 1
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid - 1]:  # mid在递减部分,向左边查找
                end = mid - 1
            else:  # mid在递增部分,向右边查找
                start = mid + 1


if __name__ == '__main__':
    with open('75.in') as f:
        arr = eval(f.read())
    # arr = [1, 2, 3, 8, 10, 7]
    # arr = [100, 102, 104, 7, 9, 11, 4, 3]
    print(Solution().findPeak(arr))  # 99999
    print(Solution().findPeak_1(arr))  # 99999
