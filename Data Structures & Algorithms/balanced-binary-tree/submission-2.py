# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node: return 0
            return 1 + max(dfs(node.left), dfs(node.right))
        
        if not root: return True
        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)

        if abs(leftHeight - rightHeight) > 1: return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        return left and right

        
