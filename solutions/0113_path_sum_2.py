from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, path, sum):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and sum == targetSum:
                answers.append(list(path))
                return

            backtrack(node.left, path, sum + node.val)
            backtrack(node.right, path, sum + node.val)

            path.pop()

        answers = []
        backtrack(root, [], targetSum)

        return answers
