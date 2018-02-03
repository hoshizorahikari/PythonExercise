'''
167. 链表求和
知识点：链表；难度：简单；高频题++
你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。
样例:给出两个链表 3->1->5->null (513)和 5->9->2->null(295)，返回 8->0->8->null(808)
'''

from hikari_tool import ListNode, SingleLinkedList


class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2 
    """

    def addLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 先处理第1个结点
        s = l1.val + l2.val
        head = ListNode(s % 10)
        tag = s // 10  # tag记录是否进位
        cur = head
        while l1.next and l2.next:
            s = l1.next.val + l2.next.val + tag
            cur.next = ListNode(s % 10)
            tag = s // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        # 只要有一个next为空，就处理另外一个
        while l1.next:
            s = l1.next.val + tag
            cur.next = ListNode(s % 10)
            tag = s // 10  # 但此时tag大部分情况为0...
            cur = cur.next
            l1 = l1.next
        while l2.next:
            s = l2.next.val + tag
            cur.next = ListNode(s % 10)
            tag = s // 10
            cur = cur.next
            l2 = l2.next
        # 此时l1.next和l2.next都是空，可能出现进位的情况，直接构造新的结点挂在后面
        if tag:
            cur.next = ListNode(tag)
        return head


if __name__ == '__main__':
    l1 = SingleLinkedList([5, 5])  # 55
    l2 = SingleLinkedList([7, 5])  # 57
    l3 = SingleLinkedList()
    l3.head = Solution().addLists(l1.head, l2.head)
    l3.travel()  # [2, 1, 1]也就是112
