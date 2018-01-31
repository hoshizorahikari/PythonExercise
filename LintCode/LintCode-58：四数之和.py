"""
58. 四数之和
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。
 注意事项:四元组(a, b, c, d)中，需要满足a <= b <= c <= d
答案中不可以包含重复的四元组。
样例:例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：
[(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)]
标签 ：排序 数组 两根指针 哈希表
"""


class Solution:
    """
    @param: numbers: Give an array
    @param: target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        n = len(numbers)
        numbers.sort()  # 排序之后处理简单
        lst = []
        # 三层循环好像不太好...
        for i in range(n - 3):  # i<=j<=k<=l
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    s = numbers[i] + numbers[j] + numbers[k] + numbers[l]
                    if s == target:
                        tup = (numbers[i], numbers[j], numbers[k], numbers[l])
                        if tup not in lst:
                            lst.append(tup)
                    if s >= target:
                        l -= 1
                    if s <= target:
                        k += 1
        return lst


if __name__ == '__main__':
    s = Solution()
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(s.fourSum(arr, target))  # [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
