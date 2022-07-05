"""
1200. 最小绝对差
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        best, ans = arr[-1] - arr[0], []
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            delta = b - a
            if delta < best:
                best, ans = delta, [[a, b]]
            elif delta == best:
                ans.append([a, b])
        return ans


if __name__ == '__main__':
    s = Solution()
    arr = [i * 1000000000000 for i in range(1000000)]
    print(s.minimumAbsDifference(arr))
