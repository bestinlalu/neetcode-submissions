# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = 1

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val):
            if not root:
                return
            max_val = max(root.val, max_val)
            
            if root.left and max_val <= root.left.val:
                self.res += 1
            if root.right and max_val <= root.right.val:
                self.res += 1

            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, float('-infinity'))
        return self.res
        