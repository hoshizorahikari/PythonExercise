"""
写一个算法来判断一个数是不是"快乐数"。
一个数是不是快乐是这么定义的：对于一个正整数，
每一次将该数替换为他每个位置上的数字的平方和，
然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。
如果可以变为1，那么这个数就是快乐数。
样例：19 就是一个快乐数。
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
标签：哈希表 数学
"""

class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        lst = []
        while n != 1:
            tmp = 0
            for i in str(n):
                tmp += int(i) ** 2
            if tmp in lst:
                return False
            lst.append(tmp)
            n = tmp
        return True


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 100):
        if s.isHappy(i):
            print(i, end=' ')  # 1 7 10 13 19 23 28 31 32 44 49 68 70 79 82 86 91 94 97 
    print()
