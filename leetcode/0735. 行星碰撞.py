"""
给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/asteroid-collision
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            while ans and i < 0 < ans[-1]:
                if -i > ans[-1]:
                    ans.pop()
                else:
                    if -i == ans[-1]:
                        ans.pop()
                    break
            else:
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([-4, -1, 10, 2, -1, 8, -9, -6, 5, 2]))
