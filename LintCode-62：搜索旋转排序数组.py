"""
难度：中等；知识点：数组、二分法；高频题+
假设有一个排序的按未知的旋转轴旋转的数组(比如，[0, 1, 2, 4, 5, 6, 7]可能成为[4, 5, 6, 7, 0, 1, 2])。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。可以假设数组中不存在重复元素。
样例：给出[4, 5, 1, 2, 3]，target=1返回2；target=0，返回-1
"""

class Solution:
    def search(self, A, target):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            # 原数组可以看为两个递增的数组, 一分为二肯定有一边是递增的
            # 如果target在递增区域, 将搜索范围减小至递增区域, 否则去另一边搜索
            if A[start] < A[mid]:  # start~mid递增
                if A[start] <= target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # mid~end递增
                if A[end] >= target > A[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
        
        
if __name__ == '__main__':
    s = Solution()
    arr = [0, 1, 2, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    target = -10
    print(s.search(arr, target))  # 3
    # LintCode此方法测试时间为605ms；A.index(target)用时670ms，所以有意思吗？

