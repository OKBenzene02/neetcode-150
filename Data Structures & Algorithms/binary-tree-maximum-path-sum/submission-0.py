# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxSum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root: return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.maxSum = max(self.maxSum, left + right + root.val)
            return root.val + max(left, right)
        dfs(root)
        return self.maxSum