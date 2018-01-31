"""
15. 全排列
给定一个数字列表，返回其所有可能的排列。
注意事项:你可以假设没有重复数字。
样例:给出一个列表[1,2,3]，其全排列为：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
挑战 :使用递归和非递归分别解决。
标签 :领英 递归
"""


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if len(nums) < 2:
            return [nums]
        # 先获取除最后一个元素的全排列
        pre = self.permute(nums[:-1])
        lst = []
        last = nums[-1]
        # 再将最后一个元素插入里面每个列表的每个位置
        for arr in pre:
            for j in range(len(arr) + 1):  # 0~len都可以插入
                tmp = [x for x in arr]  # 复制一份再插入
                tmp.insert(j, last)
                lst.append(tmp)
        return lst


if __name__ == '__main__':
    s = Solution()
    arr = [x + 1 for x in range(4)]
    print(s.permute(arr))  # 大列表里有n!个长度为n的小列表
    """
    [[4, 3, 2, 1], [3, 4, 2, 1], [3, 2, 4, 1], [3, 2, 1, 4], [4, 2, 3, 1], [2, 4, 3, 1], [2, 3, 4, 1], 
    [2, 3, 1, 4], [4, 2, 1, 3], [2, 4, 1, 3], [2, 1, 4, 3], [2, 1, 3, 4], [4, 3, 1, 2], [3, 4, 1, 2],
    [3, 1, 4, 2], [3, 1, 2, 4], [4, 1, 3, 2], [1, 4, 3, 2], [1, 3, 4, 2], [1, 3, 2, 4], [4, 1, 2, 3],
    [1, 4, 2, 3], [1, 2, 4, 3], [1, 2, 3, 4]]
    """
