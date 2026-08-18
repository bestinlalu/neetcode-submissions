"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        m = {}

        def bfs(node):
            q = collections.deque()
            q.append(node)

            while q:
                old_node = q.popleft()
                if old_node not in m:
                    m[old_node] = Node(old_node.val, [])
                for n in old_node.neighbors:
                    if n not in m:
                        q.append(n)
                        m[n] = Node(n.val, [])
                    m[old_node].neighbors.append(m[n])

        bfs(node)
        return m[node]
