# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pre_idx = 0
        indexMap = {}
        for idx, node in enumerate(inorder):
            indexMap[node] = idx

        def dfs(l, r) -> TreeNode:
            if l > r:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(val)
            mid = indexMap[val]
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node

        return dfs(0, len(inorder) - 1)
