class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            j = d.get(nums[i], None)

            if (j != None and j != i):
                return [j, i]
            
            d[diff] = i

        return []