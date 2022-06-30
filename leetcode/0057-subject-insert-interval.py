"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        first = newInterval[0]
        last = newInterval[1]

        def get_index(x, flag=0):
            left = 0
            right = n - 1
            while right >= left:
                mid = (right + left) // 2
                if x < intervals[mid][flag]:
                    right = mid - 1
                elif x > intervals[mid][flag]:
                    left = mid + 1
                else:
                    return mid
            return left

        first_index = get_index(first)
        last_index = get_index(last, -1)
        if first_index > 0 and first <= intervals[first_index - 1][1]:
            first = intervals[first_index - 1][0]
            first_index = first_index - 1
        if last_index < n and last >= intervals[last_index][0]:
            last = intervals[last_index][1]
            last_index = last_index + 1
        intervals[first_index:last_index] = [[first, last]]
        return intervals


if __name__ == '__main__':
    s = Solution()
    # print(s.insert([[1, 3], [6, 9], [10, 15]], [2, 10]))
    # print(s.insert([[1, 3], [6, 9], [10, 15]], [2, 15]))
    # print(s.insert([[1, 3], [6, 9], [10, 15]], [4, 5]))
    # print(s.insert([[1, 3], [6, 9], [10, 15]], [2, 5]))
    print(s.insert([[1, 5]], [1, 3]))
    print(s.insert([[1, 3], [6, 9]], [2, 5]))
