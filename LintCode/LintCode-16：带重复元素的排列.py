"""
16. 带重复元素的排列
给出一个具有重复数字的列表，找出列表所有不同的排列。
样例:给出列表 [1,2,2]，不同的排列有：
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
挑战 :使用递归和非递归分别完成该题。
标签 :领英 递归 深度优先搜索
"""


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if len(nums) < 2:
            return [nums]
        # 先获取除最后一个元素的全排列
        pre = self.permuteUnique(nums[:-1])
        lst = []
        last = nums[-1]
        # 再将最后一个元素插入里面每个列表的每个位置
        for arr in pre:
            for j in range(len(arr) + 1):  # 0~len都可以插入
                tmp = [x for x in arr]  # 复制一份再插入
                tmp.insert(j, last)
                if tmp not in lst:  # 判断是否重复
                    lst.append(tmp)
        return lst


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 3]
    print(s.permuteUnique(arr))
    # [[3, 2, 2, 1], [2, 3, 2, 1], [2, 2, 3, 1], [2, 2, 1, 3], [3, 2, 1, 2], [2, 3, 1, 2], [2, 1, 3, 2], [2, 1, 2, 3], [3, 1, 2, 2], [1, 3, 2, 2], [1, 2, 3, 2], [1, 2, 2, 3]]
