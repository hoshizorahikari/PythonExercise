'''
35. 翻转链表
知识点：链表；难度：简单；高频题++
翻转一个链表
样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
'''
from random import randint
from hikari_tool import SingleLinkedList


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        new_head = None
        while head:
            next = head.next  # 记录旧链表当前结点的下一个结点, 防止找不到原来链表
            head.next = new_head  # 旧链表当前结点next指向前面结点(新链表头结点), 这步为反转
            new_head = head  # new_head移到新链表头结点
            head = next  # head为工作指针后移
        return new_head


if __name__ == '__main__':
    s = Solution()
    arr = [randint(10, 99) for x in range(10)]
    ll = SingleLinkedList(arr)
    ll.travel()  # [35, 70, 44, 79, 89, 59, 74, 65, 80, 82]
    ll.head = s.reverse(ll.head)
    ll.travel()  # [82, 80, 65, 74, 59, 89, 79, 44, 70, 35]
