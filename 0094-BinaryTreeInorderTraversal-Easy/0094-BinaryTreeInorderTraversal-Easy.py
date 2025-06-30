# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历就是 左->根->右 这样的顺序
        res = []
        
        def order(root):
            if not root:
                return
            order(root.left)
            res.append(root.val)
            order(root.right)
        
        order(root)
        return res
        