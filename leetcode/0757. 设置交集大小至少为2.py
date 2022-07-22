"""
一个整数区间[a, b](a < b) 代表着从a到b的所有连续整数，包括a和b。

给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。

输出这个最小集合S的大小。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/set-intersection-size-at-least-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(reverse=True)
        s = []
        for i in intervals:
            num = 2
            for a in s:
                if num == 0:
                    break
                if i[0] <= a <= i[1]:
                    num -= 1
            else:
                ans += num
                for j in range(num):
                    b = i[0] + j
                    while b in s:
                        b += 1
                    s.append(b)
        return ans


# 答案
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
    # print(s.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
    print(s.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
    # print(s.intersectionSizeTwo([[1, 3], [4, 9], [0, 10], [6, 7], [1, 2], [0, 6], [7, 9], [0, 1], [2, 5], [6, 8]]))
