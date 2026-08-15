# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            level = []
            for i in range(l):
                ele = q.popleft()
                if ele:
                    level.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)

            if level:
                res.append(level)

        return res

        