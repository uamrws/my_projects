"""
我们要把给定的字符串 S从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组widths，这个数组widths[0] 代表 'a' 需要的单位，widths[1] 代表 'b' 需要的单位，...，widths[25] 代表 'z' 需要的单位。

现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-lines-to-write-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row_num, last_row_len = 1, 0
        for i in s:
            w = widths[ord(i) - ord('a')]
            last_row_len += w
            if last_row_len > 100:
                row_num += 1
                last_row_len = w

        return [row_num, last_row_len]


if __name__ == '__main__':
    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    s = Solution()
    print(s.numberOfLines(
        [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "bbbcccdddaaa"
    ))
