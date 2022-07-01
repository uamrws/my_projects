"""
给你一个由数字和运算符组成的字符串expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import cache
from typing import List
import operator


class Solution:
    """

    f(1,n) = f(1,n-1)*f(n,n) + f(1,n-2)*f(n-1,n)+f(1,n-3)*f(n-2,n)+...+f(1,1)*f(2,n)

    """
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        s = ""
        nums = []
        ops = []
        for i in expression:
            if i in self.operations:
                nums.append(int(s))
                ops.append(self.operations[i])
                s = ""
            else:
                s += i
        nums.append(int(s))

        @cache
        def compute(x, y):
            if x == y:
                return [nums[x]]
            ans = []
            for i in range(1, y + 1):
                for a in compute(x, y - i):
                    for b in compute(y - i + 1, y):
                        ans.append(ops[y - i](a, b))
            return ans

        return compute(0, len(nums) - 1)


class Solution:
    """

    f(1,n) = f(1,n-1)*f(n,n) + f(1,n-2)*f(n-1,n)+f(1,n-3)*f(n-2,n)+...+f(1,1)*f(2,n)

    """
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        s = ""
        nums = []
        ops = []
        for i in expression:
            if i in self.operations:
                nums.append(int(s))
                ops.append(self.operations[i])
                s = ""
            else:
                s += i
        nums.append(int(s))

        n = len(ops)
        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i].append(num)

        for y in range(n):
            for i in range(1, y + 1):
                for a in compute(x, y - i):
                    for b in compute(y - i + 1, y):
                        ans.append(ops[y - i](a, b))

        @cache
        def compute(x, y):
            if x == y:
                return [nums[x]]
            ans = []
            for i in range(1, y + 1):
                for a in compute(x, y - i):
                    for b in compute(y - i + 1, y):
                        ans.append(ops[y - i](a, b))
            return ans

        return compute(0, n - 1)


if __name__ == '__main__':
    expression = "2*3-4*5"
    s = Solution()
    print(s.diffWaysToCompute(expression))
