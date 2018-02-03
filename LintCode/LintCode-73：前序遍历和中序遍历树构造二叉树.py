"""
根据前序遍历和中序遍历树构造二叉树.
注意事项：你可以假设树中不存在相同数值的节点
样例：给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:
  2
 / \
1   3
"""

from hikari_tool import BinaryTree, TreeNode


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """

    def buildTree(self, preorder, inorder):
        if set(preorder) != set(inorder):
            return
        if len(preorder) == 0:
            return
        root_num = preorder[0]  # 前序遍历第1个为根结点
        root = TreeNode(root_num)
        pos = inorder.index(root_num)  # 寻找根结点在中序遍历的位置
        # 对左右子树分别递归
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return root


if __name__ == '__main__':
    preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7]
    inorder = [8, 4, 9, 2, 5, 1, 6, 3, 7]
    tree = BinaryTree()
    tree.root = Solution().buildTree(preorder, inorder)
    tree.breadth_travel()  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
