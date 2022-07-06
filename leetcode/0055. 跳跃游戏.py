"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx, ln = 0, len(nums) - 1
        for i, n in enumerate(nums):
            if mx >= ln:
                return True
            if mx < i:
                return False
            mx = max(i + n, mx)


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
