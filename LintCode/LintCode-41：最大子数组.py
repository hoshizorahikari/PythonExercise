"""
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
注意事项:子数组最少包含一个数
样例:给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
"""


class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        max_sum = nums[0]  # 初始为第1个元素
        # 临时变量初始视第1个元素而定
        tmp = nums[0] if nums[0] > 0 else 0

        for i in range(1, len(nums)):  # 如果前面和tmp大则赋值给max_sum, 否则如果前面小于0则舍弃,因为无法使后面更大
            tmp += nums[i]
            if tmp > max_sum:
                max_sum = tmp
            elif tmp < 0:
                tmp = 0
        return max_sum


if __name__ == '__main__':
    arr1 = [-4, -3, -5, -7, -2]
    arr2 = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    arr3 = [5, -10, 4]
    with open('41.in') as f:
        arr4 = eval(f.read())
    print(Solution().maxSubArray(arr1))  # -2
    print(Solution().maxSubArray(arr2))  # 6
    print(Solution().maxSubArray(arr3))  # 5
    print(Solution().maxSubArray(arr4))  # 302

