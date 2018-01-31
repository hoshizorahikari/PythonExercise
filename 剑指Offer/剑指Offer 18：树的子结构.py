"""
剑指offer
树的子结构
题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：约定空树不是任意一个树的子结构）
"""

from hikari_tool import TreeNode, BinaryTree


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        # 先以根结点为起点比较是否包含tree2, 没有再分别以左右子树为起点比较
        return self.compare(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def compare(self, pRoot1, pRoot2):
        if pRoot2 is None:  # tree2遍历完, 完全匹配
            return True
        if pRoot1 is None:  # tree2未完全匹配, tree1已经遍历完
            return False
        if pRoot1.val != pRoot2.val:  # 根结点对应值不匹配
            return False
        # 根结点值相同再比较左右子树
        return self.compare(pRoot1.left, pRoot2.left) and self.compare(pRoot1.right, pRoot2.right)


if __name__ == '__main__':
    s = Solution()
    tree1 = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    tree2 = BinaryTree([2, 4, 5])
    tree3 = BinaryTree([4, 5, 6])
    print(s.HasSubtree(tree1.root, tree2.root))  # True
    print(s.HasSubtree(tree1.root, tree3.root))  # False
