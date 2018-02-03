"""
78. 最长公共前缀
给k个字符串，求出他们的最长公共前缀(LCP)
样例:在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"
        在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"
标签 :LintCode 版权所有 字符串处理 基本实现 枚举法
"""


class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:  # 列表为空返回空字符串
            return ''
        length = len(strs)
        if length == 1:  # 只有一个字符串直接返回
            return strs[0]
        # 拿第1个字符串与剩余字符串逐位比较
        for x in range(len(strs[0])):
            for i in range(1, length):
                # 可能后面存在短字符串, 如果等于长度或有字符不匹配, 直接返回
                if x >= len(strs[i]) or strs[0][x] != strs[i][x]:
                    return strs[0][:x]
        return strs[0]  # 此处为第1个字符串全部匹配


if __name__ == '__main__':
    lst = ["ABCDEFG", "ABCEFG", "ABCEFA", 'AB']
    lst2 = ["ABCD", "ABEF", "ACEF", 'CBA']
    s = Solution()
    print('-{}-'.format(s.longestCommonPrefix(lst)))  # -AB-
    print('-{}-'.format(s.longestCommonPrefix(lst2)))  # --
