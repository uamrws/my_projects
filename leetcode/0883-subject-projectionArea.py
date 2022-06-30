"""
在n x n的网格grid中，我们放置了一些与 x，y，z 三轴对齐的1 x 1 x 1立方体。

每个值v = grid[i][j]表示 v个正方体叠放在单元格(i, j)上。

现在，我们查看这些立方体在 xy、yz和 zx平面上的投影。

投影就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for x in range(n):
            x_z_area = 0
            y_z_area = 0
            for y in range(n):
                z = grid[x][y]
                zz = grid[y][x]
                if z != 0:
                    ans += 1
                if z > x_z_area:
                    x_z_area = z
                if zz > y_z_area:
                    y_z_area = zz
            ans += x_z_area
            ans += y_z_area
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[1, 0], [0, 2]]))
