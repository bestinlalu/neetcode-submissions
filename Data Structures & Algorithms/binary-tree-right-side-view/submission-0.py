# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            r = None
            for i in range(l):
                ele = q.popleft()
                if ele:
                    r = ele
                    q.append(ele.left)
                    q.append(ele.right)
            if r:
                res.append(r.val)
        
        return res
        