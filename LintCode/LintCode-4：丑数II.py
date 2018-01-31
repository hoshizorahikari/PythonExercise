"""
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
注意：可以认为1也是一个丑数
样例：如果n = 9， 返回 10
挑战：要求时间复杂度为O(nlogn)或者O(n)
标签 ：LintCode 版权所有 优先队列
"""


class Solution:
    """
        @param: n: An integer
        @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        if n < 7:  # 1~6都是丑数
            return n
        arr = [1]
        p2, p3, p5 = 0, 0, 0
        while True:
            s2 = 2 * arr[p2]
            s3 = 3 * arr[p3]
            s5 = 5 * arr[p5]
            tmp = min(s2, s3, s5)
            arr.append(tmp)
            if tmp == s2:
                p2 += 1
            if tmp == s3:
                p3 += 1
            if tmp == s5:
                p5 += 1
            if len(arr) == n:
                return arr[-1]


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 21):
        print((i, s.nthUglyNumber(i)), end=' ')
    print()
    # (1, 1) (2, 2) (3, 3) (4, 4) (5, 5) (6, 6) (7, 8) (8, 9) (9, 10) (10, 12) (11, 15) (12, 16) (13, 18) (14, 20) (15, 24) (16, 25) (17, 27) (18, 30) (19, 32) (20, 36)
