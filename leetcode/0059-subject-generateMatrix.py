"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for i in range(n)]
        m = n
        r = 0
        c = -1
        flag = 1
        num = 1
        while m and n:
            for _ in range(n):
                c += flag
                ans[r][c] = num
                num += 1
            for _ in range(m - 1):
                r += flag
                ans[r][c] = num
                num += 1
            flag = -flag
            m -= 1
            n -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
