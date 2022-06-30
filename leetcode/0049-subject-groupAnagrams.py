"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import string
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            hash_slot = [0] * 26
            for i in map(lambda x: ord(x) - 97, s):
                hash_slot[i] += 1
            mp.setdefault(tuple(hash_slot), []).append(s)
        return list(mp.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    s.groupAnagrams(strs)
