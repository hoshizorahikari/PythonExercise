"""
64. 合并排序数组
合并两个排序的整数数组A和B变成一个新的数组。
注意：可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
样例：给出 A = [1, 2, 3, empty, empty], B = [4, 5]
合并之后 A 将变成 [1,2,3,4,5]
标签 ：数组 排序数组 脸书
"""


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # 从后面开始,比较A和B的元素,将较大的添加到A最后
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        # A和B有一个为空将另一个添加到A的前面
        while m > 0:
            A[m + n - 1] = A[m - 1]
            m -= 1
        while n > 0:
            A[m + n - 1] = B[n - 1]
            n -= 1

    def mergeSortedArray_2(self, A, m, B, n):
        # 结果LintCode测试两个方法用时一样
        for i in range(n):
            A[m + i] = B[i]
        A.sort()


if __name__ == '__main__':
    a = [2, 6, 7, None, None]
    b = [1, 4]
    Solution().mergeSortedArray(a, 3, b, 2)
    print(a)  # [1, 2, 4, 6, 7]
