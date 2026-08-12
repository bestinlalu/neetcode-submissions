import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if (len(B) < len(A)):
            A, B = B, A
        
        l = 0
        r = len(A)
        total = len(A) + len(B)
        half = total // 2
        print(A, B, l, r)

        while l <= r:
            m = (l + r) // 2
            n = half - m
            # print(l, r, m, n)

            l1 = A[m - 1] if (m - 1) >= 0 else float('-infinity')
            r1 = A[m] if m < len(A) else float('infinity')
            l2 = B[n - 1] if (n - 1) >= 0 else float('-infinity')
            r2 = B[n] if n < len(B) else float('infinity')

            print(l1, r1, l2, r2)

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = m - 1
            else:
                l = m + 1
        return -1
        