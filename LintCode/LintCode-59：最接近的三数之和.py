"""
59. 最接近的三数之和
给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。
 注意事项:只需要返回三元组之和，无需返回三元组本身
样例:例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.
挑战 :O(n^2) 时间, O(1) 额外空间。
标签 :排序 数组 两根指针
"""


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        n = len(numbers)
        numbers.sort()  # 排序之后处理简单
        # 记录开始的三数之和与和目标的差值
        s0 = numbers[0] + numbers[1] + numbers[2]
        close = abs(s0 - target)
        for i in range(n - 2):  # i<=j<=k
            # 根据s的大小，移动指针j和k
            j = i + 1
            k = n - 1
            while j < k:
                s = numbers[i] + numbers[j] + numbers[k]
                tmp = abs(s - target)
                if tmp < close:  # 如果与目标差值更小则替换
                    s0 = s
                    close = tmp
                if s >= target:
                    k -= 1
                if s <= target:
                    j += 1
        return s0


if __name__ == '__main__':
    s = Solution()
    arr = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2]
    target = 7
    print(s.threeSumClosest(arr, target))  # 4
