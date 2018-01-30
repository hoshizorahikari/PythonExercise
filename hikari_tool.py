class TreeNode():
    """单个结点"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class BinaryTree():
    """二叉树"""

    def __init__(self, arr=None):
        self.root = None
        if arr:
            self.build_tree(arr)

    def build_tree(self, arr):
        """自己瞎写的，构造二叉树"""
        if not arr:
            return None
        self.root = TreeNode(arr.pop(0))
        queue = [self.root]
        while arr:
            cur = queue.pop(0)
            tmp = arr.pop(0)
            if tmp == '#':
                cur.left = None
            else:
                cur.left = TreeNode(tmp)
                queue.append(cur.left)
            if not arr:
                return
            tmp = arr.pop(0)

            if tmp == '#':
                cur.right = None
            else:
                cur.right = TreeNode(tmp)
                queue.append(cur.right)

    # def breadth_travel(self, root):
    #     """利用队列实现树的层次遍历"""
    #     lst = []
    #     if root is None:
    #         return lst
    #     queue = [root]
    #     while queue:
    #         cur_node = queue.pop(0)
    #         lst.append(cur_node.val)
    #         if cur_node.left:
    #             queue.append(cur_node.left)
    #         if cur_node.right:
    #             queue.append(cur_node.right)
    #     return lst
    
    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        lst = []
        if self.root is None:
            print(lst)
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            lst.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print(lst)

    # def preorder(self, root):
    #     """先序遍历非递归"""
    #     if root is None:
    #         return []
    #     lst = []
    #     stack = []
    #     cur = root
    #     while True:
    #         while cur:
    #             stack.append(cur)
    #             lst.append(cur.val)
    #             cur = cur.left
    #         if stack:
    #             cur = stack.pop()
    #             cur = cur.right
    #         if not cur and not stack:
    #             return lst
             
    def preorder(self):
        """先序遍历非递归"""
        lst = []
        if self.root is None:
            print(lst)
            return
        stack = []
        cur = self.root
        while True:
            while cur:
                stack.append(cur)
                lst.append(cur.val)
                cur = cur.left
            if stack:
                cur = stack.pop()
                cur = cur.right
            if not cur and not stack:
                print(lst)
                return

    # def inorder(self, root):
    #     """中序遍历非递归"""
    #     if root is None:
    #         return []
    #     lst = []
    #     stack = [] # 使用栈作为临时容器
    #     cur = root
    #     while True:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left# 先访问左子树
    #         if stack:# 访问到最左边没元素了, 开始出栈
    #             cur = stack.pop()
    #             lst.append(cur.val)# 从栈中弹出是第2次遇到cur结点
    #             cur = cur.right# 再访问右子树
    #         if not cur and not stack:
    #             return lst# cur为None栈为空表示遍历完成
    
    def inorder(self):
        """中序遍历非递归"""
        lst = []
        if self.root is None:
            print(lst)
            return
        stack = []
        cur = self.root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                lst.append(cur.val)
                cur = cur.right
            if not cur and not stack:
                print(lst)
                return

    # def postorder(self, root):
    #     """后序遍历递归"""
    #     lst = []
    #     self.__postorder_helper(root, lst)
    #     return lst
    
    def postorder(self):
        """后序遍历递归"""
        lst = []
        self.__postorder_helper(self.root, lst)
        print(lst)

    def __postorder_helper(self, root, lst):
        if root is None:
            return
        self.__postorder_helper(root.left, lst)
        self.__postorder_helper(root.right, lst)
        lst.append(root.val)


class ListNode():
    """单个结点的实现"""

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList():
    """单链表的实现"""

    def __init__(self, arr=None):
        self.head = None
        if arr is not None:
            self.build_linked_list(arr)

    def __lt__(self, other):
        return self.head.val < other.head.val

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """获取链表长度"""
        # current游标，用来移动遍历结点，工作指针后移思想
        current = self.head
        cnt = 0
        while 1:
            if not current:  # 空链表情况符合
                return cnt
            cnt += 1
            current = current.next

    def travel(self):
        """遍历整个链表"""
        print(self.get_lst())

    def build_linked_list(self, arr):
        """根据列表构建链表"""
        self.head = None
        for i in arr:
            self.append(i)

    def get_lst(self):
        """根据链表获取列表"""
        current = self.head
        lst = []
        while current:
            lst.append(current.val)
            current = current.next
        return lst

    def add_first(self, item):
        """链表头部添加元素"""
        node = ListNode(item)
        # 空链表也满足
        node.next = self.head
        self.head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = ListNode(item)
        current = self.head
        # 空链表为特殊情况
        if self.is_empty():
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 添加位置小于等于0就当添加到链表头部
        if pos < 1:
            self.add_first(item)
        # 添加位置大于等于length就当添加到链表尾部
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = ListNode(item)
            pre = self.head
            cnt = 0
            while 1:
                if cnt == pos - 1:
                    node.next = pre.next
                    pre.next = node
                    return
                cnt += 1
                pre = pre.next

    def remove(self, item):
        """删除指定结点"""
        current = self.head
        pre = None
        # 特殊情况删除第1个结点，只有1个结点也符合
        if current.val == item:
            self.head = current.next
            return
        # 空链表什么也不做符合；删除尾部结点也符合
        while current:
            if current.val == item:
                pre.next = current.next
                return
            pre = current
            current = current.next

    def pop(self, pos=-1):
        """根据位置删除结点"""
        if 0 > pos > -self.length() - 1:
            return self.pop(self.length() + pos)
        current = self.head
        cnt = 0
        pre = None
        if pos == 0:
            self.head = current.next
            return current.val
        while current:
            if cnt == pos:
                pre.next = current.next
                return current.val
            pre = current
            current = current.next
            cnt += 1

    def search(self, item):
        """查找指定结点是否存在"""
        current = self.head
        cnt = 0
        while current:
            if current.val == item:
                return cnt
            current = current.next
            cnt += 1
        return -1

    def get(self, pos):
        """根据位置获取结点"""
        current = self.head
        cnt = 0
        if pos < 0 or pos > self.length() - 1:
            return None
        while current:
            if cnt == pos:
                return current.val
            current = current.next
            cnt += 1


class CycleLinkedList():
    """循环单链表"""

    def __init__(self, arr=None):
        self.rear = None
        if arr is not None:
            self.build(arr)

    def is_empty(self):
        """判空"""
        return self.rear is None

    def prepend(self, val):
        """前端插入"""
        node = ListNode(val)
        if self.is_empty():
            node.next = node
            self.rear = node  # 建立只有一个结点的环
        else:
            node.next = self.rear.next
            self.rear.next = node

    def append(self, val):
        """后端插入"""
        self.prepend(val)
        self.rear = self.rear.next  # 相当于前端插入, 再把尾指针移到第一个

    def pop(self):
        """前端弹出"""
        if self.is_empty():
            print('循环链表为空！')
            return
        first = self.rear.next
        if first is self.rear:  # 只有一个结点
            self.rear = None
        else:
            self.rear.next = first.next  # 最后一个结点的next指向第2个结点
        return first.val

    def get_list(self):
        """从第1个开始转为列表"""
        lst = []
        if self.is_empty():
            return lst
        cur = self.rear.next
        while True:
            lst.append(cur.val)
            if cur is self.rear:  # 遇到尾结点停止
                return lst
            cur = cur.next

    def travel(self):
        """从第1个结点开始打印循环链表元素"""
        print(self.get_list())

    def build(self, arr):
        """构建循环链表"""
        for i in arr:
            self.append(i)


class Stack():
    """栈"""

    def __init__(self):
        self.__lst = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__lst.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.__lst:
            return self.__lst.pop()
        return None

    def peek(self):
        """返回栈顶元素"""
        if self.__lst:
            return self.__lst[-1]
        return None

    def is_empty(self):
        """判断栈是否为空"""
        return not self.__lst

    def __len__(self):
        """返回栈的元素个数"""
        return len(self.__lst)


class Queue():
    """队列"""

    def __init__(self):
        self.__lst = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__lst.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        if self.__lst:
            return self.__lst.pop(0)
        return None

    def is_empty(self):
        """判断一个队列是否为空"""
        return not self.__lst

    def __len__(self):
        """返回队列的大小"""
        return len(self.__lst)


class PrioQueue():
    def __init__(self, lst=()):
        self.__elems = list(lst)
        if lst:  # 不为空就构造堆
            self.build_heap()

    def __len__(self):
        return len(self.__elems)

    def is_empty(self):
        """判断堆是否为空"""
        return not self.__elems

    def peek(self):
        """获取堆顶元素"""
        if not self.is_empty():
            return self.__elems[0]

    def enqueue(self, elem):
        """入队"""
        self.__elems.append(None)  # 先不赋值, 加入None占位
        self.siftup(elem, len(self.__elems) - 1)

    def siftup(self, elem, end):
        """向上筛选"""
        cur = end  # cur开始为最后位置
        parent = (cur - 1) // 2  # parent为cur的父结点
        # 父结点比当前结点大就下移
        while cur > 0 and elem < self.__elems[parent]:
            self.__elems[cur] = self.__elems[parent]
            cur = parent  # 两个指针上移
            parent = (cur - 1) // 2
        # 结束时cur为合适位置, 赋值为elem
        self.__elems[cur] = elem

    def dequeue(self):
        """出队"""
        if self.is_empty():
            print('优先队列为空！')
            return
        elem = self.__elems[0]  # 记录最优先元素后面需要返回
        last_elem = self.__elems.pop()  # last_elem为最后的元素, 移到堆顶向下筛选
        if self.__elems:
            self.siftdown(last_elem, 0, len(self.__elems))
        return elem  # 返回被删除的最优先元素

    def siftdown(self, elem, begin, length):
        """向下筛选"""
        child = 2 * begin + 1  # child开始为begin的左儿子
        while child < length:  # child小于length说明存在左儿子
            right = child + 1  # begin右儿子
            # 如果存在右儿子并且右儿子比左儿子小
            if right < length and self.__elems[right] < self.__elems[child]:
                child += 1  # child移到右儿子, 即左右儿子较小的
            if elem < self.__elems[child]:
                break  # 如果最后元素比当前最小儿子小的话, 说明位置正确, 直接退出循环
            # 否则下面小元素上移
            self.__elems[begin] = self.__elems[child]
            begin = child  # 两个指针向下筛选
            child = 2 * child + 1
        # 结束时begin为合适位置赋值为elem
        self.__elems[begin] = elem

    def build_heap(self):
        """构建堆"""
        length = len(self.__elems)
        # 从下面往上面构造, 从最后一个结点的父结点开始到根结点0
        for i in range(length // 2 - 1, -1, -1):
            self.siftdown(self.__elems[i], i, length)

    def travel(self):
        """遍历堆"""
        print(self.__elems)
