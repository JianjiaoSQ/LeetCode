# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def same(new_left, new_right):
            if not new_left or not new_right:
                return new_left is new_right
            return new_left.val == new_right.val and same(new_left.left, new_right.right) and same(new_left.right, new_right.left)
        
        return same(root.left, root.right)
        