"""
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 CBTInserter 类:

CBTInserter(TreeNode root)使用头节点为root的给定树初始化该数据结构；
CBTInserter.insert(int v) 向树中插入一个值为Node.val == val的新节点TreeNode。使树保持完全二叉树的状态，并返回插入节点TreeNode的父节点的值；
CBTInserter.get_root() 将返回树的头节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/complete-binary-tree-inserter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self._root = root
        self._deque = deque()
        self._deque.append(root)

    def insert(self, val: int) -> int:
        while self._deque:
            node = self._deque[0]
            if not node.left:
                node.left = TreeNode(val)
                return node.val
            elif not node.right:
                node.right = TreeNode(val)
                return node.val
            self._deque.popleft()
            self._deque.append(node.left)
            self._deque.append(node.right)

    def get_root(self) -> TreeNode:
        return self._root


# 答案
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.cnt = 0

        q = deque([root])
        while q:
            self.cnt += 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        self.cnt += 1

        child = TreeNode(val)
        node = self.root
        highbit = self.cnt.bit_length() - 1

        for i in range(highbit - 1, 0, -1):
            if self.cnt & (1 << i):
                node = node.right
            else:
                node = node.left

        if self.cnt & 1:
            node.right = child
        else:
            node.left = child

        return node.val

    def get_root(self) -> TreeNode:
        return self.root


if __name__ == '__main__':
    root = TreeNode(1)
    s = CBTInserter(root)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.insert(5)
    print(s.get_root())
