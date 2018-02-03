"""
83. 落单的数 II
给出3*n + 1 个的数字，除其中一个数字之外其他每个数字均出现三次，找到这个数字。
样例:给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4
挑战:一次遍历，常数级的额外空间复杂度
标签:贪心
"""


class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumberII_1(self, A):
        """字典,lintcode居然超时了, 这台垃圾电脑秒出结果"""
        dct = {}
        for i in A:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for k, v in dct.items():
            if v == 1:
                return k

    def singleNumberII_2(self, A):
        """逗比答案, 还是超时"""
        for i in A:
            if A.count(i) == 1:
                return i

    def singleNumberII_3(self, A):
        """不用怀疑还是超时..."""
        lst1 = []
        lst2 = []
        for i in A:
            if i not in lst1:
                if i not in lst2:
                    lst1.append(i)
            else:
                if i not in lst2:
                    lst2.append(i)
                else:
                    lst1.remove(i)
        return lst1[0]

    def singleNumberII(self, A):
        """位运算就没有超时,但是Python对于负数貌似有问题"""
        ret = 0
        bits = [0] * 32
        # 将列表每个数字转为32位二进制, 对应位置相加
        for n in A:
            for i in range(32):
                bits[i] += n >> i & 1
        # 出现3次的数二进制每个位置都是3的倍数
        # 对3取余得落单的数的32位二进制
        for i in range(32):
            ret += (bits[i] % 3) << i  # 将32位二进制数累加为十进制
        return ret
        # ret = 0
        # bits = [0] * 32
        # for i in range(32):
        #     for n in A:
        #         bits[i] += n >> i & 1
        #     bits[i] = bits[i] % 3
        #     ret = ret | bits[i] << i
        # return ret


if __name__ == '__main__':
    s = Solution()
    arr = [-1, -2, -3] * 3 + [-4]
    print(s.singleNumberII(arr))  # 4294967292,Python对于负数貌似有问题,使用Java没问题
