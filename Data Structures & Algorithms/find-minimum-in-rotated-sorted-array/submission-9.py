class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while(l <= r):
            mid = (l + r) // 2
            res = min(res, nums[mid])
            res = min(res, nums[r])
            if(nums[mid] < nums[l]):
                r = r - 1
            else:
                l = l + 1
        return res