"""
103. 带环链表 II
给定一个链表，如果链表中存在环，则返回到链表中环的起始节点，如果没有环，返回null。
样例：给出 -21->10->4->5, tail connects to node index 1，返回10
挑战 ：不使用额外的空间
标签 ：两根指针 链表
"""
from hikari_tool import SingleLinkedList, CycleLinkedList


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle_2(self, head):
        # 超时了...
        p = head
        cnt = 0
        while p:  # p每次往后移一下
            p = p.next
            cnt += 1
            count = 0
            q = head
            while q != p:  # q每次从头开始跑,直到遇到p
                q = q.next
                count += 1
            if count != cnt:  # 计数不等说明有环
                return p

    def detectCycle(self, head):
        """
        快慢指针fast与slow在圆中c处相遇，slow走过x+y，fast走过2(x+y)或者x+y+kC(圆的周长)；
        所以2x+2y=x+y+kC-->y=kC-x；这样fast从起点a重新单步前进到切点b走x步，
        而slow从c绕圆走x步，加上之前的总共2x+y=x+kC步，也是在b处；
        所以重整后fast和slow单步前进肯定在b处相遇，即要返回的结点。

        """
        if head is None or head.next is None:
            return
        # 快慢指针判断有没有环
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        if fast and fast == slow:
            # fast从头开始跑,slow继续跑,两者同速,它们一定会在环起点相遇
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast


if __name__ == '__main__':
    ll = SingleLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(Solution().detectCycle(ll.head))  # None
    p = ll.head
    while p.next:
        p = p.next
    p.next = CycleLinkedList([45, 32, 67, 23, 12]).rear
    print(Solution().detectCycle(ll.head).val)  # 12
