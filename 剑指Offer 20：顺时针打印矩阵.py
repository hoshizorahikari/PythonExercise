"""
剑指offer 20 顺时针打印矩阵
题目描述:输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution():
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ret = []
        if not matrix:
            return ret
        while True:
            ret.extend(matrix.pop(0))  # 每次pop第1行
            if not matrix:
                break
            matrix = self.turn(matrix)  # 顺时针旋转二维矩阵,还是pop第1行,直到矩阵为空
        return ret

    def turn(self, matrix):
        """顺时针旋转二维矩阵"""
        rows = len(matrix)
        cols = len(matrix[0])
        new_matrix = []
        for col in range(cols):
            tmp = []
            for row in range(rows):
                tmp.append(matrix[row][col])  # 将一列元素放入一个数组,也就是一行
            new_matrix.append(tmp)
        # 列变为行属于逆时针旋转,逆序好变为顺时针
        new_matrix.reverse()
        return new_matrix


if __name__ == '__main__':
    s = Solution()
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = [[1, 2], [3, 4], [5, 6]]
    print(s.printMatrix(matrix))  # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
