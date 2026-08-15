# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    is_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if abs(l - r) > 1:
                self.is_balanced = False
            
            return 1 + max(l, r)
        
        dfs(root)
        return self.is_balanced