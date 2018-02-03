"""
96. 链表划分
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
应该保留两部分链表节点原有的相对顺序。
样例：给定链表 1->4->3->2->5->2->null，并且 x=3
返回 1->2->2->4->3->5->null
标签：两根指针 链表
"""
from hikari_tool import SingleLinkedList, ListNode


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None or head.next is None:
            return head
        # 随意建立两个头结点,方便操作
        big = ListNode('big')
        small = ListNode('small')
        p = head
        bp, sp = big, small
        while p:
            if p.val >= x:  # 大的接在big后面
                bp.next = p
                bp = bp.next
            else:  # 小的接在small后面
                sp.next = p
                sp = sp.next
            p = p.next
        sp.next = big.next  # 大的接在小的后面
        bp.next = None  # 防止有环
        return small.next


if __name__ == '__main__':
    arr = [1, 4, 3, 2, 5, 2]
    ll = SingleLinkedList(arr)
    ll.head = Solution().partition(ll.head, 3)
    ll.travel()  # [1, 2, 2, 4, 3, 5]
