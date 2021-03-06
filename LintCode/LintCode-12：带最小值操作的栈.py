'''
实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
注意事项：如果堆栈中没有数字则不能进行min方法的调用
样例：如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1
'''


class MinStack:
    def __init__(self):
        self.__lst = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.__lst.append(number)

    """
    @return: An integer
    """

    def pop(self):
        return self.__lst.pop()

    """
    @return: An integer
    """

    def min(self):
        return min(self.__lst)


if __name__ == '__main__':
    s = MinStack()
    s.push(1)
    print(s.pop())
    s.push(2)
    s.push(3)
    print(s.min())
    s.push(1)
    print(s.min())
