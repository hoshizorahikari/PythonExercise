"""
84. 落单的数 III
给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。
样例:给出 [1,2,2,3,4,4,5,3]，返回 1和5
挑战 :O(n)时间复杂度，O(1)的额外空间复杂度
标签 :贪心 LintCode 版权所有
"""


class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """

    def singleNumberIII_1(self, A):
        # 不用怀疑又超时了
        lst = []
        for i in A:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)
        return lst

    def singleNumberIII(self, A):
        ans = 0
        for i in A:
            ans ^= i  # ans最后为所有数字异或结果, 也是两个落单数异或结果
        k = 0
        # 寻找两个落单数二进制最小不同位置k
        # 异或相同为0不同为1, 结果最低位为1的就是不同位置k
        while ans % 2 == 0:  # 一直右移看是不是偶数
            k += 1
            ans >>= 1
        r1, r2 = 0, 0
        # A中, r1和r2的k位置不同, 有2n1个与r1的k位置相同,2n2个与r2的k位置相同, n1+n2=n
        # 将r1和n1个数做两次异或得到r1; 将r2和n2个数做两次异或得到r2
        for i in A:
            kbit = (i >> k) % 2
            if kbit:
                r2 ^= i
            else:
                r1 ^= i
        return [r1, r2]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 3, 4, 4, 5, 3]
    print(s.singleNumberIII(arr))  # [1, 5]
    with open('84.in') as f:
        arr = eval(f.read())
    print(len(arr))  # 31976
    print(s.singleNumberIII(arr))  # [3036501, 1802237]
