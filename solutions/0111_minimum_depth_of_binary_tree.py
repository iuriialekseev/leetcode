from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return 0

        if root.left is None:
            return 1 + self.dfs(root.right)
        elif root.right is None:
            return 1 + self.dfs(root.left)

        return 1 + min(self.dfs(root.left), self.dfs(root.right))
