# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        d = {}

        while head is not None:
            p = d.get(head, None)

            if p is None:
                d[head] = head.val
            else:
                return True
            head = head.next

        return False
        