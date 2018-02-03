"""
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。
样例:给出 [1,2,2,1,3,4,3]，返回 4
挑战 :一次遍历，常数级的额外空间复杂度
标签:贪心

"""


class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumber_1(self, A):
        """第1次出现加入列表,第2次出现从列表删除,剩余的为落单的数"""
        lst = []
        for i in A:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)
        return lst[0]

    def singleNumber(self, A):
        """异或"""
        ret = 0
        for i in A:
            ret ^= i
        return ret


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 1, 3, 4, 3]
    print(s.singleNumber(arr))
