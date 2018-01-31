"""
33. N皇后问题
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。
给定一个整数n，返回所有不同的n皇后问题的解决方案。
每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。
样例:对于4皇后问题存在两种解决的方案：
[
    [".Q..", // Solution 1
     "...Q",
     "Q...",
     "..Q."],
    ["..Q.", // Solution 2
     "Q...",
     "...Q",
     ".Q.."]
]
挑战:你能否不使用递归完成？
标签:递归 深度优先搜索
"""


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        lst = list(self.queens(n))  # 生成器转为列表
        ret = []
        for tup in lst:
            tmp = []
            for i in tup:
                s = ['.'] * n
                s[i] = 'Q'
                tmp.append(''.join(s))
            ret.append(tmp)
        return ret

    def conflict(self, pre, col):
        """判断下一次要放入的皇后(cur,col)与当前棋盘的皇后是否冲突"""
        cur = len(pre)  # 当前棋盘皇后数量, 也是要下一次要放的行数
        for row in range(cur):  # 0~cur-1行与cur行比较
            # 列之差绝对值等于0或行之差为冲突
            if abs(pre[row] - col) in (0, cur - row):
                return True
        return False

    def queens(self, num, pre=()):
        for col in range(num):
            if not self.conflict(pre, col):
                if len(pre) == num - 1:
                    yield (col,)  # 最后一次结果传给上一次递归
                else:
                    # 后面的元组层层向上传递, 组成为新的元组, 直到最开始调用,
                    # 将完整元组返回给solveNQueens中的调用, 结果是生成器
                    for ret in self.queens(num, pre + (col,)):  # 当前行不冲突则递归下一行
                        yield (col,) + ret


if __name__ == '__main__':
    s = Solution()
    lst = s.solveNQueens(8)
    for i in lst:
        print(lst.index(i) + 1)
        for j in i:
            print(j)
