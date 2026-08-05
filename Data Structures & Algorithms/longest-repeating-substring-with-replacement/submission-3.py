class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = j = 0
        d = defaultdict(int)
        maxk = 0
        nj = -1

        while(i <= j and j < len(s)):
            if nj != j: 
                d[s[j]] += 1
                nj = j
            maxf = 0
            maxf = max(maxf, max(d.values()))
            
            if (j - i + 1 - maxf) <= k:
                maxk = max(maxk, j - i + 1)
                j += 1
            else:
                d[s[i]] -= 1
                i += 1

        return maxk
        
        