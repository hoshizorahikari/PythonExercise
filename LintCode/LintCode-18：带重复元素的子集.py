"""
给定一个可能具有重复数字的列表，返回其所有可能的子集
注意事项
子集中的每个元素都是非降序的
两个子集间的顺序是无关紧要的
解集中不能包含重复子集

样例
如果 S = [1,2,2]，一个可能的答案为：
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
import copy


class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        lst = self.subsetsWithDup(nums[:-1])  # 先获取前len-1个子集
        tmp = copy.deepcopy(lst)  # 将子集深拷贝一份

        for i in lst:
            i.append(nums[-1])  # 再子集基础上添加最后一个元素, 排序
            i.sort()
        for i in tmp:  # 将备份的子集中不存在于lst的子集放进去
            if i not in lst:
                lst.append(i)

        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([2, 1, 2, 1, 3]))
    # [[1, 1, 2, 3], [1, 1, 2, 2, 3], [1, 2, 3], [1, 2, 2, 3], [1, 1, 3], [1, 3], [2, 3], [2, 2, 3], [3], [1, 1, 2], [1, 1, 2, 2], [1, 2], [1, 2, 2], [1, 1], [1], [2], [2, 2], []]
