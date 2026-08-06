class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
            
        d = defaultdict(int)

        for c in s1:
            d[c] += 1
            
        i = 0
        j = len(s1) - 1

        while(j < len(s2)):
            t = defaultdict(int)
            k = i
            while(k <= j):
                t[s2[k]] += 1
                k += 1
            if(d.items() == t.items()):
                return True
            j += 1
            i += 1

        return False