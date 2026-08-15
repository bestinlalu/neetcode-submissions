# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    is_subRoot = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(tree, subTree):
            if not tree and not subTree:
                return
            elif (not tree and subTree) or (not subTree and tree) or (subTree and tree and subTree.val != tree.val):
                self.is_subRoot = False
                return
            sameTree(tree.left, subTree.left)
            sameTree(tree.right, subTree.right)


        def dfs(root, subRoot):
            if not root or not subRoot:
                return
            if root.val == subRoot.val:
                self.is_subRoot = True
                sameTree(root, subRoot)
            if not self.is_subRoot:
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)
            
            
        dfs(root, subRoot)
        return self.is_subRoot

            
        