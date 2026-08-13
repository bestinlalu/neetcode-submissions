"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dc = {}
        traverse = head
        while traverse:
            node = Node(traverse.val, None, None)
            dc[(traverse)] = node
            traverse = traverse.next

        traverse = head
        while traverse:
            nxt_key = traverse.next
            nxt = dc[nxt_key] if nxt_key else None
            ran_key = traverse.random
            random = dc[ran_key] if ran_key else None
            node = dc[traverse]
            node.next = nxt
            node.random = random

            dc[traverse] = node
            traverse = traverse.next

        return dc[head] if dc else None

        
        
        


        