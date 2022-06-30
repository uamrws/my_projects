"""
357. 统计各位数字都不同的数字个数
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n。
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(12))
