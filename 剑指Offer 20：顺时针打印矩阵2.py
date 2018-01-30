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
    def printMatrix(self, matrix):
        ret = []
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0 or cols == 0:
            return ret
        # 四个变量记录二维矩阵的范围
        left, top, right, bottom = 0, 0, cols - 1, rows - 1
        while right >= left and bottom >= top:
            # 从左到右, 每次都改变四个变量的值, 所以在循环里也要判断
            for i in range(left, right + 1):
                ret.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # 从上往下
            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # 从右到左
            for i in range(right, left - 1, -1):
                ret.append(matrix[bottom][i])
            bottom -= 1
            # 从下往上
            if bottom >= top:
                for i in range(bottom, top - 1, -1):
                    ret.append(matrix[i][left])
                left += 1
        return ret

    def printMatrix_2(self, matrix):
        ret = []
        if not matrix:
            return ret
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0 or cols == 0:
            return ret
        start = 0
        while rows > 2 * start and cols > 2 * start:
            endx, endy = cols - 1 - start, rows - 1 - start
            # 从左到右,m[0][0]~m[0][endx],0为最外层,start从0到最里层
            for i in range(start, endx + 1):
                ret.append(matrix[start][i])
            # print(ret)
            # 从上到下,m[1][endx]~m[endy][endx]
            if start < endy:
                for i in range(start + 1, endy + 1):
                    ret.append(matrix[i][endx])
            # 从右向左,m[endy][endx-1]~m[endy][0]
            if start < endx and start < endy:
                for i in range(endx - 1, start - 1, -1):
                    ret.append(matrix[endy][i])
            # 从下到上,m[endy-1][0]~m[1][0]
            if start < endx and start < endy - 1:
                for i in range(endy - 1, start, -1):
                    ret.append(matrix[i][start])
            start += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # matrix = [[1, 2], [3, 4], [5, 6]]
    # matrix=[[1]]
    # matrix = [[1], [2], [3], [4], [5]]
    # matrix = [[1, 2, 3]]
    print(s.printMatrix_2(matrix))  # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print(s.printMatrix(matrix))  # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
