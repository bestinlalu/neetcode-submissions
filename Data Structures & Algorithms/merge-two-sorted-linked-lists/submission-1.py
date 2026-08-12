# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        A, B = list1, list2
        p, q = 0, 0
        head, curr = None, None

        while A is not None or B is not None:
            if A is None or (B is not None and A.val > B.val):
                if curr is not None:
                    curr.next = B
                    curr = B
                else:
                    curr = B
                    head = curr
                B = B.next
                q += 1
            elif B is None or (A is not None and A.val <= B.val):
                if curr is not None:
                    curr.next = A
                    curr = A
                else:
                    curr = A
                    head = curr
                A = A.next
                p += 1

        return head
            
        