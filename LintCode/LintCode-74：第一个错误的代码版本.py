"""
74. 第一个错误的代码版本
代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。
你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，具体接口详情和调用方法请见代码的注释部分。
 注意：请阅读上述代码，对于不同的语言获取正确的调用 isBadVersion 的方法，比如java的调用方式是SVNRepo.isBadVersion(v)
样例：给出 n=5
调用isBadVersion(3)，得到false
调用isBadVersion(5)，得到true
调用isBadVersion(4)，得到true
此时我们可以断定4是第一个错误的版本号
挑战 ：调用 isBadVersion 的次数越少越好
标签 ：LintCode 版权所有 二分法 脸书
"""
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""


class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        if id < 5:  # 测试用,5为第1个错误版本
            return False
        return True


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # 自己写的,此题LintCode有中文注释会报错?
        if SVNRepo.isBadVersion(1):  # 如果第1个就是错误,返回1
            return 1
        start, end = 1, n
        # 二分查找
        while start <= end:
            mid = (start + end) // 2
            if SVNRepo.isBadVersion(mid):
                if not SVNRepo.isBadVersion(mid - 1):
                    return mid  # 如果mid为错误,mid-1为正确,则找到第1个错误版本
                end = mid - 1
            else:
                start = mid + 1

    def findFirstBadVersion_2(self, n):
        if n <= 0:
            return 0
        start, end = 1, n
        while start < end:
            mid = start + (end - start) // 2
            # mid = (start + end) // 2  # 这两个貌似都可以
            if SVNRepo.isBadVersion(mid):
                end = mid  # 如果mid为错误版本end=mid,因为mid可能是第1个错误版本
            else:
                start = mid + 1  # 如果mid不是错误版本,那么就在mid后面找
        # 结束时,start==end,都是第1个错误版本
        return start


if __name__ == '__main__':
    print(Solution().findFirstBadVersion(10))  # 5
