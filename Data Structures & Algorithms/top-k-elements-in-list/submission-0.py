class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)
        b = [[] for _ in range(0, len(nums) + 1)]

        for n in nums:
            d[n] += 1
        
        for key, value in d.items():
            b[value].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for j in b[i]:
                res.append(j)
                if len(res) == k:
                    return res

        