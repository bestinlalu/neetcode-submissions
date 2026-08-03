class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        for t in range(len(nums)):
            i = t + 1
            j = len(nums) - 1
            
            if (t > 0 and nums[t] == nums[t - 1]):
                continue

            while (i < j):
                su = nums[t] + nums[i] + nums[j]

                if su > 0:
                    j -= 1
                elif su < 0:
                    i += 1
                else:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while(nums[i] == nums[i - 1] and i < j):
                        i += 1

        return res
        