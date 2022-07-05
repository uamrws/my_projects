"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 1:
            return
        k %= n
        nums[:n - k], nums[k:] = nums[n - k:], nums[:n - k]


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    print(s.rotate(nums, 200))
    print(nums)
