class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
            
        d = defaultdict(int)

        for c in s1:
            d[c] += 1
        u = len(d.keys())
        i = 0
        j = len(s1) - 1

        while(j < len(s2)):
            t = defaultdict(int)
            k = i
            p = 0
            while(k <= j):
                t[s2[k]] += 1
                if(t[s2[k]] == d[s2[k]]):
                    p += 1
                k += 1
            print(u, p)
            if(u == p):
                return True
            j += 1
            i += 1

        return False