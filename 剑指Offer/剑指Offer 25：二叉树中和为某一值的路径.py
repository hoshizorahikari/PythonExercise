# 题目：输入一棵二叉树和一个整数，打印二叉树中结点值的和为输入整数的所有路径。路径为从树根结点开始往下一直到叶结点所经过的结点形成一条路径。
# 思路：前序遍历访问结点值，如果是叶结点并路径结点和与输入整数相等，将路径以数组形式添加到要返回的二维数组中；如果不是叶结点，则继续访问其子结点；
# 当前结点访问结束，使用递归可以回退到其父结点；路径回退时应该在路径数组中删除当前结点。保存路径数据结构实际上是一个栈，就是递归的本质。
# 使用一个变量记录当前路径的和略麻烦，可以使用输入整数减去路径上结点的值，当减到0的时候说明当前路径结点值的和与输入整数相等。

from hikari_tool import BinaryTree
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        self.ret = []
        self.curPath = []
        self.dsfFind(root, expectNumber)
        return self.ret
    def dsfFind(self, root, num):
        if root is None:
            return
        # 先序遍历的顺序添加结点的值,如果当前和等于目标,且为叶结点就复制到ret
        self.curPath.append(root.val)
        num -= root.val
        if num == 0 and root.left is None and root.right is None:
            self.ret.append([x for x in self.curPath])
        if root.left:
            self.dsfFind(root.left, num)
        if root.right:
            self.dsfFind(root.right, num)
        self.curPath.pop()  # 删除最后元素,路径回退
if __name__ == '__main__':
    tree = BinaryTree([10, 5, 12, 4, 7])
    print(Solution().FindPath(tree.root, 22))  # [[10, 5, 7], [10, 12]]

