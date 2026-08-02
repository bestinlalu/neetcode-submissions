class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            n = d.get(i, None)
            if n == None:
                d[i] = 1
            else:
                return True
        return False