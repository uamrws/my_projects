"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N & 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N >>= 1
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)



if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 77))
