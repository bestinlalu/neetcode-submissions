# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = 1

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return
            if root.left:
                if root.val <= root.left.val:
                    self.res += 1
                root.left.val = max(root.val, root.left.val) 
            if root.right:
                if root.val <= root.right.val:
                    self.res += 1
                root.right.val = max(root.val, root.right.val) 
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res
        