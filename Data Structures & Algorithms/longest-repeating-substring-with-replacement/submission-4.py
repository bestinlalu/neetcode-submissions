class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = j = 0
        d = defaultdict(int)
        maxk = 0

        while(i <= j and j < len(s)):
            d[s[j]] += 1
            maxf = 0
            maxf = max(maxf, max(d.values()))
            
            if (j - i + 1 - maxf) <= k:
                maxk = max(maxk, j - i + 1)
            else:
                d[s[i]] -= 1
                i += 1
            j += 1
        return maxk
        
        