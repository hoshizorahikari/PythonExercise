"""
93. 平衡二叉树
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。
样例：给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}
A)  3            B)    3
   / \                    \
 9  20                  20
    /  \                 /  \
  15   7             15  7
二叉树A是高度平衡的二叉树，但是B不是
标签：分治法 递归
"""
from hikari_tool import BinaryTree


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # 自己写的,太乱了
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True  # 左右都为空,高度差为0,返回true
        if root.left and root.right is None:
            if root.left.left or root.left.right:
                return False  # 右儿子为空,左儿子有儿子,高度差为2,false
            return True  # 高度差为1,true
        if root.right and root.left is None:
            if root.right.left or root.right.right:
                return False  # 左儿子为空,右儿子有儿子,高度差为2,false
            return True  # 高度差为1,true
        # 递归左右子树
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced_2(self, root):
        # 最终返回不是-1表示求得树高,是平衡的;-1表示没求得树高,不是平衡的
        return self.getDepth(root) != -1

    def getDepth(self, root):
        # 求树的高度,如果发现左右子树高度差大于1,则不平衡,直接返回-1
        # 以后遇到-1的情况,也直接返回-1而不求树的高度
        if root is None:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1


if __name__ == '__main__':
    arr = [3, 9, 20, '#', '#', 15, 7]
    tree = BinaryTree(arr)
    print(Solution().isBalanced(tree.root))  # True
    arr1 = [3, '#', 20, 15, 7]
    tree = BinaryTree(arr1)
    print(Solution().isBalanced(tree.root))  # False
