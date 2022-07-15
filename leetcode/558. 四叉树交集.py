"""

二进制矩阵中的所有元素不是 0 就是 1 。

给你两个四叉树，quadTree1 和 quadTree2。其中 quadTree1 表示一个 n * n 二进制矩阵，而 quadTree2 表示另一个 n * n 二进制矩阵。

请你返回一个表示 n * n 二进制矩阵的四叉树，它是 quadTree1 和 quadTree2 所表示的两个二进制矩阵进行 按位逻辑或运算 的结果。

注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(1, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)

        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
            return Node(top_left.val, True)

        return Node(0, False, top_left, top_right, bottom_left, bottom_right)


if __name__ == '__main__':
    s = Solution()
    s.intersect(
        Node(0, 1),
        Node(0, 1),
    )
    print(1)
