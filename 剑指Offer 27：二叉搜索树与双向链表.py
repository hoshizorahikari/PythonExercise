# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。\

from hikari_tool import BinaryTree
class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree
        # 对左右子树分别递归求双向链表
        left = self.Convert(pRootOfTree.left)
        right = self.Convert(pRootOfTree.right)
        if left:  # 如果左边双向链表不为空,找到最后结点,将根结点挂在后面
            left_last = left
            while left_last.right:
                left_last = left_last.right
            left_last.right = pRootOfTree
            pRootOfTree.left = left_last
        left_last = pRootOfTree  # 不论left是否为空,此时尾指针都移到根结点
        if right:  # 如果有右边的双向链表,将其挂在根结点后面
            right.left = left_last
            left_last.right = right
        return left if left else pRootOfTree
def print_lst(head):
    cur = head
    lst = ['-->']
    while cur.right:
        lst.append(cur.val)
        cur = cur.right
    lst.append(cur.val)
    lst.append('-->')
    while cur:
        lst.append(cur.val)
        cur = cur.left
    print(lst)
if __name__ == '__main__':
    arr = [32, 16, 45, 12, 28, 40, 56, 6, '#', 25, 30, '#', '#', '#', 88]
    tree = BinaryTree(arr)
    head = Solution().Convert(tree.root)
    print_lst(head) # ['-->', 6, 12, 16, 25, 28, 30, 32, 40, 45, 56, 88, '-->', 88, 56, 45, 40, 32, 30, 28, 25, 16, 12, 6]
