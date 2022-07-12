"""
给你一个 m x n 的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个二维索引数组indices，indices[i] = [ri, ci] 指向矩阵中的某个位置，其中 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

对 indices[i] 所指向的每个位置，应同时执行下述增量操作：

ri 行上的所有单元格，加 1 。
ci 列上的所有单元格，加 1 。
给你 m、n 和 indices 。请你在执行完所有indices指定的增量操作后，返回矩阵中 奇数值单元格 的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        r_n = 0
        c_n = 0
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
            r_n += 1 if rows[r] & 1 else -1
            c_n += 1 if cols[c] & 1 else -1
        return (r_n * n + c_n * m) - 2 * (r_n * c_n)


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = cols = 0
        for r, c in indices:
            rows ^= 1 << r
            cols ^= 1 << c
        r_n, c_n = rows.bit_count(), cols.bit_count()
        return (r_n * n + c_n * m) - 2 * (r_n * c_n)


if __name__ == '__main__':
    s = Solution()
    print(
        s.oddCells(
            10000000, 10000000,
            [[random.randint(0, 64), random.randint(0, 64)] for i in range(100000)]
        ))
