# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    is_copy = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return
            if (p and not q) or (q and not p) or (p and q and p.val != q.val):
                self.is_copy = False
                return

            dfs(p.right, q.right)
            dfs(p.left, q.left)

        dfs(p, q)

        return self.is_copy