'''
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。
 注意事项：在三元组(a, b, c)，要求a <= b <= c。
结果不能包含重复的三元组。
样例：如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：
(-1, 0, 1)
(-1, -1, 2)
'''


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        n = len(numbers)
        numbers.sort()  # 排序之后处理简单
        lst = []
        for i in range(n - 2):  # i<j<k
            # 根据s的大小，移动指针j和k
            j = i + 1
            k = n - 1
            while j < k:
                s = numbers[i] + numbers[j] + numbers[k]
                if s == 0:
                    tup = (numbers[i], numbers[j], numbers[k])
                    if tup not in lst:
                        lst.append(tup)
                if s >= 0:
                    k -= 1
                if s <= 0:
                    j += 1
        return lst

if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, 4]
    arr1 = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1]
    print(Solution().threeSum(arr))  # [(-1, -1, 2), (-1, 0, 1)]
    print(Solution().threeSum(arr1))  # [(-1, 0, 1)]
