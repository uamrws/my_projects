"""
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：

MagicDictionary() 初始化对象
void buildDict(String[]dictionary) 使用字符串数组dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-magic-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from typing import List


class MagicDictionary:

    def __init__(self):
        self.m_dict = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            for j in range(len(i)):
                self.m_dict[i[:j] + "." + i[j + 1:]].append(i)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            k = searchWord[:i] + "." + searchWord[i + 1:]
            if k in self.m_dict and (searchWord not in self.m_dict[k] or len(self.m_dict[k]) > 1):
                return True
        return False


if __name__ == '__main__':
    s = MagicDictionary()
    s.buildDict(["hello", "leetcode"])
    print(s.search("hello"))
    print(s.search("hhllo"))
    print(s.search("hell"))
    print(s.search("leetcoded"))
