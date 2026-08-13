class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        f, s = 0, 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if f == s:
                break

        s2 = 0
        while True:
            s2 = nums[s2]
            s = nums[s]

            if s == s2:
                return s2

        