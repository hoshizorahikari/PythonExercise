"""
剑指offer24 二叉搜索树的后序遍历序列
题目描述:输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出true,否则输出false。假设输入的数组的任意两个数字都互不相同。

"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.verify(sequence, 0, len(sequence) - 1)

    def verify(self, lst, start, end):
        root = lst[end]  # 根结点的值
        mid = start
        # 寻找第1个比root大的元素, 此元素之前都是root的左子树
        while mid < end and lst[mid] < root:
            mid += 1
        # mid及之后元素为root右子树, 如果有小于root的元素则false
        for i in range(mid, end):
            if lst[i] < root:
                return False
        # mid==start说明没有左子树,mid==end说明没有右子树
        # 如果存在左子树或右子树则递归, 没有直接为true
        left = self.verify(lst, start, mid - 1) if mid > start else True
        right = self.verify(lst, mid, end - 1) if mid < end else True
        return left and right

    def VerifySquenceOfBST_2(self, sequence):
        if not sequence:
            return False
        i = 0
        end = len(sequence) - 1
        while end > 0:
            while sequence[i] < sequence[end]:
                i += 1
            while sequence[i] > sequence[end]:
                i += 1
            if i < end:
                return False
            i = 0
            end -= 1
        return True


if __name__ == '__main__':
    print(Solution().VerifySquenceOfBST([6, 12, 25, 30, 28, 16, 40, 88, 56, 45, 32]))  # True
    print(Solution().VerifySquenceOfBST([7, 4, 6, 5]))  # False
