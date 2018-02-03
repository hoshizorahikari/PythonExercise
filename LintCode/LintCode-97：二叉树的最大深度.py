"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。
样例：给出一棵如下的二叉树:
  1
 / \
2   3
    / \
   4   5
这个二叉树的最大深度为3.
"""
from hikari_tool import BinaryTree


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # 广度优先遍历,使用队列作为临时容器
        if root is None:
            return 0
        cnt = 0
        queue = [root]
        while queue:
            cnt += 1
            for i in range(len(queue)):  # 一次放一层结点的儿子
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return cnt


if __name__ == '__main__':
    arr = [1, 2, 3, '#', '#', 4, 5]
    tree = BinaryTree(arr)
    print(Solution().maxDepth(tree.root))  # 3
