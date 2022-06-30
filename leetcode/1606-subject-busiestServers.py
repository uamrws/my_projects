"""
你有 k个服务器，编号为 0到 k-1，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求。请求分配到服务器的规则如下：

第i（序号从 0 开始）个请求到达。
如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
如果第(i % k)个服务器空闲，那么对应服务器会处理该请求。
否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 i个服务器在忙，那么会查看第 (i+1)个服务器，第 (i+2)个服务器等等。
给你一个 严格递增的正整数数组arrival，表示第i个任务的到达时间，和另一个数组load，其中load[i]表示第i个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 最繁忙的服务器。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有最繁忙服务器序号的列表，你可以以任意顺序返回这个列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

from heapq import heappush
from heapq import heappop


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 服务器构成一个环，从环的开始到结束长度为k
        # 当第 「idx」 个请求到达，会交给服务器列表中找下标为 「idx%k」 提供服务
        # 如果该服务器处于 「busy」 的工作状态，则顺着环一直向下去找
        # 直到找到空闲的服务器 或者绕一圈回到 「idx%k-1」
        # 但是每一次都循环一圈，太过耗时
        # 所以采用下面的算法来进行

        # 1.创建一个小根堆 「available」 用来记录可用服务器，存储形式为 int:下标
        # 2.创建一个小根堆 「busy」 用来记录正在处理请求的服务器，存储形式为 tuple:(耗时，下标)
        # 3.创建一个列表 「server_nums」用来统计每个服务器提供服务的次数 ，存储形式为 int:下标

        # 4.当第 「idx」 个请求在 arrival_time 时间到达时
        # 5.首先检查「busy」中的首个服务器, 将其耗时s_cost_time与arrival_time对比
        # 6.如果s_cost_time<=arrival_time，则说明服务已经处于空闲状态
        # 7.将该服务器的下标 s_id 推回到「available」中  ******重点讲解一下这一块

        # ----7.1 从「busy」中取出的服务器 s_id 一定有 s_id < idx (必然)
        # ----7.2 要找的服务器是从「idx % k」开始的，而不是从0开始
        # ----7.3 绕一个圈寻找空闲服务，是通过 「(idx+i)% k」取余的方式进行
        # ----7.4 重新推入到available中的数 x 一定要满足 idx <= x <= idx+k 且x%k==s_id
        # ----7.5 我们现在要计算的就是x的值（python中负数处以正数的余数为正）
        # --------7.5.1  不妨设  (n-1)*k <= idx <= n*k
        # --------7.5.2  那么要使 s_id 满足7.4  idx<=x<idx+k 且x%k==s_id（x中最小的一个）
        # --------7.5.3  只需 x = (n-1) * k + s_id   (当s_id >= idx%k时)
        # --------7.5.4  或者 x =   n   * k + s_id   (当s_id < idx%k时)
        # --------7.5.5  因为 idx<=x<idx+k 所以 0<= x-idx <= k
        # --------7.5.6  => (x-idx) %k == x-idx
        # --------7.5.7  => idx + (x-idx) % k == idx + x - idx = x
        # --------7.5.8  又根据同余原理, 「当余数 >= 0 时」，如果有m|(a-b)（m能被a-b整除且m>0） 则有a % m == b%m
        # --------7.5.9  当s_id >= idx%k时 idx + (x-idx) % k = idx + ((n-1) * k + s_id - idx) %k
        # --------7.5.10 idx + (x-idx) % k == idx + ((n-1) * k + s_id - idx) %k
        # --------7.5.11 根据同余原理 ((n-1) * k + s_id - idx) %k  == (s_id - idx) %k
        # --------7.5.12 => idx + (x-idx) % k == idx + (s_id - idx) %k
        # --------7.5.12 当s_id < idx%k时 同理可证明 idx + (x-idx) % k == idx + (s_id - idx) %k
        # --------7.5.13 所以有 x = idx + (s_id - idx) %k

        # 8.综上所证，可以得出只需要将 x 也就是「idx + (s_id - idx) %k」推回available
        # 9.那么在「available」中所有的服务器下标都会时大于idx，就保证了查找服务器一定是从「idx % k」开始的

        # 10.结束对「busy」中服务器的判断后，所有可用服务器都会放入「available」
        # 11.如果「available」没有服务器，直接放弃该请求
        # 12.否则取出「available」最小的那个服务器下标，取余后得到原始下标 「s_id」
        # 13.将tuple(耗时(arrival_time+load_time)，s_id)推入busy堆中

        available = list(range(k))
        busy = []
        server_nums = [0] * k
        for idx, (start, end) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, s_id = heappop(busy)
                # 此处涉及同余定理，查看7.1处的说明
                heappush(available, idx + (s_id - idx) % k)
            if available:
                # 计算出当前最小的可用服务器的下标
                s_id = heappop(available) % k
                # 统计服务器的服务次数
                server_nums[s_id] += 1
                # 将当前服务器(耗时，下标)推入最小堆
                heappush(busy, (start + end, s_id))

        _max = max(server_nums)
        return [idx for idx, i in enumerate(server_nums) if i == _max]


if __name__ == '__main__':
    s = Solution()
    print(s.busiestServers(3, [1, 2, 3, 4], [1, 2, 1, 2]))
