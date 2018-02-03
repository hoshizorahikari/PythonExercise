"""
给定一个二叉树，判断它是否是合法的二叉查找树(BST)
一棵BST定义为：
节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。
您在真实的面试中是否遇到过这个题？ Yes
样例：一个例子：
  2
 / \
1   4
   / \
  3   5
上述这棵二叉树序列化为 {2,1,4,#,#,3,5}.
标签：分治法 递归 二叉树 二叉查找树
"""
from hikari_tool import BinaryTree


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST_2(self, root):
        self.isBST = True
        self.last_val = None
        self.validate(root)
        return self.isBST

    def validate(self, root):
        # 其实就是中序遍历的顺序
        if root is None:
            return
        # 先遍历左子树
        self.validate(root.left)
        # 判断结点的值是否比上一个值大
        if self.last_val and self.last_val >= root.val:
            self.isBST = False
            return
        # 记录最近一次中序遍历的值
        self.last_val = root.val
        # 最后遍历右子树
        self.validate(root.right)

    def isValidBST_1(self, root):
        # 获取中序遍历的列表, 判断是否严格递增
        lst = []
        self.in_order(root, lst)
        if not lst:
            return True
        for i in range(0, len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True

    def in_order(self, root, lst):
        # 获取中序遍历的列表
        if root is None:
            return
        self.in_order(root.left, lst)
        lst.append(root.val)
        self.in_order(root.right, lst)

    def isValidBST_3(self, root):
        # 非递归,使用栈作为临时容器
        if root is None:
            return True
        stack = []
        cur = root
        last_val = None
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                if last_val and last_val >= cur.val:
                    return False
                last_val = cur.val
                cur = cur.right
            if cur is None and not stack:
                return True


if __name__ == '__main__':
    # arr = [32, 16, 45, 12, 28, 40, 56, 6, '#', 25, 30, '#', '#', 50, 88]
    # arr = [2, 1, 2]
    # arr=[1]
    # arr = [10, 5, 15, '#', '#', 6, 20]
    # arr=[2,1]
    # arr = [1, '#', 2, 3]
    arr = [
        989, 982, '#', 972, '#', 947, '#', 920, '#', 903, '#', 894, '#', 881, '#', 866, '#', 864, '#', 842, '#', 841,
        '#', 796, '#', 726, '#', 647, '#', 613, 719, 593, '#', '#', '#', 590, '#', 558, '#', 554, '#', 538, '#', 512,
        '#', 504, '#', 468, 505, 467, '#', '#', '#', 456, '#', 413, '#', 331, '#', 330, 407, 320, '#', '#', '#', 312,
        '#', 306, '#', 301, '#', 274, '#', 251, '#', 235, '#', 231, '#', 222, '#', 181, '#', 93, '#', 83, '#', 73, '#',
        64, '#', 62, '#', 60, '#', 28, '#', 21, '#', 20, '#', -32, '#', -52, '#', -70, '#', -87, '#', -98, '#', -102,
        '#', -115, '#', -116, '#', -139, '#', -183, '#', -224, '#', -241, '#', -263, '#', -284, '#', -294, '#', -296,
        '#', -320, '#', -330, '#', -392, '#', -398, '#', -407, '#', -431, '#', -445, '#', -460, '#', -463, '#', -492,
        '#', -507, '#', -518, '#', -539, '#', -552, '#', -558, '#', 559, '#', -587, '#', -673, '#', -736, '#', -757,
        '#', -766, '#', -767, '#', -823, '#', -830, '#', -867, '#', -875, '#', -891, '#', -905, '#', -910, '#', -924,
        '#', -960, '#', -985, '#', -988]
    tree = BinaryTree(arr)
    s = Solution()
    print(s.isValidBST_1(tree.root))
    print(s.isValidBST_2(tree.root))
    print(s.isValidBST_3(tree.root))
