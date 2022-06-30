"""
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

注意：起始基因序列start 默认是有效的，但是它并不一定会出现在基因库中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-genetic-mutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    @staticmethod
    def check_diff(one, other):
        r = 0
        for idx, i in enumerate(one):
            if other[idx] != i:
                r += 1
        return r

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ans_dict = {start: 0}
        while ans_dict:
            k, v = ans_dict.popitem()
            j = 0
            while j < len(bank):
                o = bank[j]
                if self.check_diff(k, o) == 1:
                    bank.pop(j)
                    if end == o:
                        return v + 1
                    else:
                        ans_dict[o] = v + 1
                else:
                    j += 1
        return -1


if __name__ == '__main__':
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AAGCCCCC", "AACCCCCC"]
    # bank = ["AAAAGCCC", "AAACGCCC", "AACCGCCC", "AACCCCCC"]
    s = Solution()
    print(s.minMutation(start, end, bank))
