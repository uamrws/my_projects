"""
给定2D空间中四个点的坐标p1,p2,p3和p4，如果这四个点构成一个正方形，则返回 true 。

点的坐标pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

一个 有效的正方形 有四条等边和四个等角(90度角)。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List, Tuple


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        p1_p2__2 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        p1_p3__2 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
        p1_p4__2 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2

        if p1_p2__2 == p1_p3__2 and (p1_p2__2 + p1_p3__2) == p1_p4__2 and p2 != p3 and p1 != p4:
            return p1_p2__2 == ((p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2) == (
                        (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2)
        elif p1_p2__2 == p1_p4__2 and (p1_p2__2 + p1_p4__2) == p1_p3__2 and p2 != p4 and p1 != p3:
            return p1_p2__2 == ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) == (
                        (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2)
        elif p1_p3__2 == p1_p4__2 and (p1_p3__2 + p1_p4__2) == p1_p2__2 and p3 != p4 and p1 != p2:
            return p1_p3__2 == ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) == (
                        (p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2)
        else:
            return False


# 答案
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/valid-square/solution/you-xiao-de-zheng-fang-xing-by-leetcode-94t5m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def checkLength(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]


def checkMidPoint(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]


def calCos(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[0] + v1[1] * v2[1]


def help(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p4[0], p3[1] - p4[1])
    return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2:
            return False
        if help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if help(p1, p4, p2, p3):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [-1, 1]
    p4 = [0, 2]
    print(s.validSquare(p1, p2, p3, p4))
