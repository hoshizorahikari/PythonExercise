"""
给出一个无重叠的按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
样例:插入区间[2, 5] 到 [[1,2], [5,9]]，我们得到 [[1,9]]。
插入区间[3, 4] 到 [[1,2], [5,9]]，我们得到 [[1,2], [3,4], [5,9]]。
标签:领英 基本实现 谷歌
"""


# Definition of Interval.
class Interval():
    """区间的定义"""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return str([self.start, self.end])


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        i = 0
        while i < len(intervals):
            cur = intervals[i]
            # 新区间在当前左边, 没有交集, 在当前序号插入新区间, 直接返回
            if end < cur.start:
                intervals.insert(i, Interval(start, end))
                return intervals
            # 新区间在当前右边, 没有交集, 跳过, 与下一个区间比较
            if start > cur.end:
                i += 1
                continue
            # 新区间与当前区间有交集, 合并两者为新区间, 并删除当前区间
            else:
                start = start if start <= cur.start else cur.start  # 开始取两者较小
                end = end if end >= cur.end else cur.end  # 结束取两者较大
                intervals.pop(i)
        # 新区间与最后区间有交集或完全在最后区间的右边, 添加到最后
        intervals.append(Interval(start, end))
        return intervals


if __name__ == '__main__':
    arr = [(1, 2), (5, 9), (10, 20), (23, 26)]
    intervals = [Interval(*x) for x in arr]
    newInterval = Interval(6, 24)
    # newInterval = Interval(3, 4)
    intervals = Solution().insert(intervals, newInterval)
    lst = [(x.start, x.end) for x in intervals]
    print(lst)  # [[1, 2], [5, 26]]
