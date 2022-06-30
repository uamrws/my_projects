"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = -1
        flag = 1
        while m and n:
            for _ in range(n):
                c += flag
                ans.append(matrix[r][c])
            for _ in range(m - 1):
                r += flag
                ans.append(matrix[r][c])
            flag = -flag
            m -= 1
            n -= 1

        return ans

    def temp(self, m, n):
        ans = [[0] * n for _ in range(m)]
        a = 1
        r = 0
        c = -1
        flag = 1
        while m and n:
            for _ in range(n):
                c += flag
                ans[r][c] = a
                a += 1
            for _ in range(m - 1):
                r += flag
                ans[r][c] = a
                a += 1
            flag = -flag
            m -= 1
            n -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(s.temp(4, 4))
