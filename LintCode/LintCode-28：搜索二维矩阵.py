"""
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
您在真实的面试中是否遇到过这个题？ Yes
样例
考虑下列矩阵：
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true
挑战：O(log(n) + log(m)) 时间复杂度
标签：二分法 矩阵 雅虎
"""


class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False
        row = len(matrix) - 1
        col = len(matrix[0]) - 1

        i, j = 0, col  # 从右上角开始寻找
        while i <= row and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    # matrix = [[], [], []]
    s = Solution()
    print(s.searchMatrix(matrix, 10))
