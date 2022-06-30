"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        before = 0
        for n in nums:
            if before >= 0:
                ans = max(ans, n + before)
                before = n + before
            else:
                ans = max(ans, n)
                before = n
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
