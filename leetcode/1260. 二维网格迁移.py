"""
给你一个 m 行 n列的二维网格grid和一个整数k。你需要将grid迁移k次。

每次「迁移」操作将会引发下述活动：

位于 grid[i][j]的元素将会移动到grid[i][j + 1]。
位于grid[i][n- 1] 的元素将会移动到grid[i + 1][0]。
位于 grid[m- 1][n - 1]的元素将会移动到grid[0][0]。
请你返回k 次迁移操作后最终得到的 二维网格。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shift-2d-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for i in range(k):
            n = 0
            for row in grid:
                row.insert(0, n)
                n = row.pop()
            grid[0][0] = n
        return grid


# 答案，一维展开
class Solution:
    """
    将grid看成一个一维的长度为m*n的数组
    所有数字下标移动k，计算一维中最新的下标
    """

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 计算一维数组中最新的下标位置
                idx = (i * n + j + k) % (m * n)
                # 计算这个一维的下标在ans这个二维数组中的位置
                ans[idx // n][idx % n] = grid[i][j]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1000000000))
