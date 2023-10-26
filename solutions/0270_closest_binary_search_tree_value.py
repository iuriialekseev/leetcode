class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            val = root.val
            curr = abs(val - target)
            prev = abs(closest - target)

            if curr < prev or curr == prev and val < closest:
                closest = val

            if target < val:
                root = root.left
            else:
                root = root.right

        return closest
