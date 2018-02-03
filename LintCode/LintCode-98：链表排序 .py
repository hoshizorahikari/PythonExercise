'''
在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。
样例
给出 1->3->2->null，给它排序变成 1->2->3->null.
'''

from random import randint
from hikari_tool import ListNode, SingleLinkedList


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        fast, slow = head, head
        # 快慢指针寻找中间结点
        while fast and fast.next:
            slow_parent = slow
            slow = slow.next
            fast = fast.next.next
        slow_parent.next = None  # 链表一分为二
        left = self.sortList(head)
        right = self.sortList(slow)
        # 使用归并排序
        return self.merge(left, right)

    def merge(self, left, right):
        head = ListNode('hikari')  # 随意创建头结点防止链表丢失
        cur = head
        # 不用头结点需要判断left和right第1个结点哪个小
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            # 一个为空, 添加另外一个结点至尾部
            if left is None:
                cur.next = right
            if right is None:
                cur.next = left
        return head.next

if __name__ == '__main__':
    s = Solution()
    arr = [randint(10, 99) for x in range(10)]
    ll = SingleLinkedList(arr)
    ll.travel()  # [42, 12, 46, 37, 81, 36, 90, 34, 27, 54]
    ll.head = s.sortList(ll.head)
    ll.travel()  # [12, 27, 34, 36, 37, 42, 46, 54, 81, 90]
