"""
剑指Offer 22：栈的压入、弹出序列
题目：输入两个整数序列，第一个序列表示栈的压入顺序，判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如：序列[1, 2, 3, 4, 5]是某栈的压入顺序，序列[4, 5, 3, 2, 1]是该压栈序列对应的一个弹出序列，但[4, 3, 5, 1, 2]就不可能是该压栈序列的弹出序列。
注意：这两个序列的长度是相等的
思路：用一个辅助栈模拟栈操作，将第1个序列元素依次入栈，栈顶元素与第2个序列第1个元素比较，如果相同则出栈，再用栈顶元素与第2个序列下一个元素比较；
如果不同则继续入栈，直到第1个序列元素全部入栈。最终如果辅助栈为空，表示第2个序列可由第1个序列进行入栈、出栈操作得到。
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV or len(pushV) != len(popV):
            return False
        stack = []  # 辅助栈
        pop_index = 0  # 弹出序列下标
        for i in pushV:
            stack.append(i)
            # 如果辅助栈顶元素等于当前弹出栈的元素, 辅助栈出栈并将弹出栈的索引后移
            while stack and stack[-1] == popV[pop_index]:
                stack.pop()
                pop_index += 1
        return stack == []


if __name__ == '__main__':
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # True
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # False
