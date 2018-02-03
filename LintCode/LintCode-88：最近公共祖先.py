"""
给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。
最近公共祖先是两个节点的公共的祖先节点且具有最大深度。
注意事项：假设给出的两个节点都在树中存在
样例：对于下面这棵二叉树
  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
"""

from hikari_tool import BinaryTree


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return
        if root == A or root == B:
            return root
        # 递归求左子树的lca和右子树的lca
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        # 如果两者不为空, root为lca
        if left and right:
            return root
        # 否则非空的为lca
        return left if left else right


if __name__ == '__main__':
    arr = [4, 3, 7, '#', '#', 5, 6]
    tree = BinaryTree(arr)
    lca = Solution().lowestCommonAncestor(tree.root, 5, 6)
    print(lca.val)  # 7
