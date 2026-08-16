# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    kmin = float('infinity')
    p = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if (not root.left and self.p == 0) or (self.p != 0):
                self.p += 1
            if self.p == k:
                self.kmin = root.val
                return
            dfs(root.right)

        dfs(root)
        return self.kmin
            


        