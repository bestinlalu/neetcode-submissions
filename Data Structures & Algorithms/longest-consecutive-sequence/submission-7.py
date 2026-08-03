class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        l = 0

        for i in nums:
            if i - 1 in s:
                continue
            m = 0
            while (i + m) in s:
                m += 1
            l = max(l, m)

        return l
