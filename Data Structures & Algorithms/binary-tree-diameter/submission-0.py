# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    max_height = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            self.max_height = max(self.max_height, l + r)
            return 1 + max(l, r)

        dfs(root)
        return self.max_height
        