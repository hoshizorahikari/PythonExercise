"""
难度：简单；知识点：数组、二分法；高频题
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引；如果没有，返回到它将会被按顺序插入的位置。假设在数组中无重复元素。
样例：[1,3,5,6]：5→2；2→1；7→4；0→0
"""


class Solution:
    def searchInsert(self, A, target):
        # 空列表直接返回0
        if not A:
            return 0
        start = 0
        end = len(A) - 1
        mid = 0
        # 二分查找寻找target的位置
        while start <= end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid + 1
            elif A[mid] > target:
                end = mid - 1
            else:
                return mid
        # 如果不存在, 比较mid处和target的大小决定插入位置
        if A[mid] > target:
            return mid
        return mid + 1
        
        
if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 6]
    print(s.searchInsert(arr, 7))  # 4
    print(s.searchInsert(arr, 0))  # 0
