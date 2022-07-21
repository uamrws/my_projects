"""
给你二叉树的根结点root，此外树的每个结点的值要么是 0 ，要么是 1 。

返回移除了所有不包含 1 的子树的原二叉树。

节点 node 的子树为 node 本身加上所有 node 的后代。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-pruning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0:
                node.left = None
            if right == 0:
                node.right = None
            if node.val == left == right == 0:
                return 0
            return 1

        dfs(root)
        if root.left or root.right or root.val:
            return root

# 答案
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    s = Solution()
    print(
        s.pruneTree(
            TreeNode(
                1,
                None,
                TreeNode(
                    0,
                    TreeNode(0),
                    TreeNode(1)
                )
            )
        ) ==
        TreeNode(
            1,
            None,
            TreeNode(
                0,
                None,
                TreeNode(1)
            )
        )
    )
