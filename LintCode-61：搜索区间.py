"""
难度：中等；知识点：数组、二分法；高频题
给定一个包含n个整数的排序数组，找出给定目标值target的起始和结束位置
如果目标值不在数组中，则返回[-1, -1]
样例：给出[5, 7, 7, 8, 8, 10]和目标值target=8，返回[3, 4]
"""

class Solution:
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        # 二分查找, 寻找target位置
        while start <= end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid + 1
            elif A[mid] > target:
                end = mid - 1
            else:
                start, end = mid, mid
                # 找到之后往左边和右边扩展, 看看有没有相同的
                while start > 0 and A[start - 1] == A[mid]:
                    start -= 1
                while end < len(A) - 1 and A[end + 1] == A[mid]:
                    end += 1
                return [start, end]
        return [-1, -1]
        
        
if __name__ == '__main__':
    s = Solution()
    arr = [5, 7, 7, 8, 8, 10]
    target = 7
    print(s.searchRange(arr, target))  # [1, 2]
