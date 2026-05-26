# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node: Optional[TreeNode]) -> int:
            if not node: return 0
            return 1 + max(height(node.left), height(node.right))

        if not root: return 0
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        return max(leftDiameter, rightDiameter, leftHeight + rightHeight)