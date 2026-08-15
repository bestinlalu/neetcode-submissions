# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return
            if root.val < p.val and root.val < q.val:
                dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left)
            else:
                self.res = root
        
        dfs(root)
        return self.res

        