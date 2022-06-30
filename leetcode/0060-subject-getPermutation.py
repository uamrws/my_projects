"""
给出集合[1,2,3,...,n]，其所有元素共有n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定n 和k，返回第k个排列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        总共只有n阶乘个数字
        要想知道首个数字是多少
        只需将k整除n-1阶乘即可
        依次计算出后续


        """
        ans = ""
        nums = [str(i) for i in range(1, n + 1)]
        m = n - 1
        while len(ans) < n:
            fact = math.factorial(m)
            idx = (k-1) // fact
            x = nums.pop(idx)
            ans += x
            if k >= fact:
                k -= fact * idx
            if k == 0:
                ans += "".join(nums[::-1])
            if k == 1:
                ans += "".join(nums)
            m -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 6))
