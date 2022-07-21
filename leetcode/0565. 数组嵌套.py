"""索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/array-nesting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans_list = [-1] * n
        max_ans = 0

        def get_ans(idx):
            if ans_list[idx] != -1:
                return ans_list[idx]
            ans_list[idx] = 0
            ans = ans_list[idx] = get_ans(nums[idx]) + 1
            return ans

        for i in nums:
            ans = get_ans(i)
            if ans == n:
                return n
            if ans > max_ans:
                max_ans = ans
        return max_ans


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_ans = 0
        flags = [False] * n

        for i in nums:
            ans = 0
            while not flags[i]:
                flags[i] = True
                ans += 1
                i = nums[i]
            max_ans = max(max_ans, ans)
        return max_ans


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_ans = 0

        for i in range(n):
            ans = 0
            while nums[i] < n:
                ans += 1
                nums[i], i = n, nums[i]
            max_ans = max(max_ans, ans)
        return max_ans


if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
