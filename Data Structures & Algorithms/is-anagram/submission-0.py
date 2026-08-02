class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d1 = {}
        d2 = {}

        if (len(s) != len(t)):
            return False
        
        for i in range(0, len(s)):

            p = d1.get(s[i], None)
            q = d2.get(t[i], None)

            if(p != None):
                d1[s[i]] = p + 1
            else:
                d1[s[i]] = 1
            if(q != None):
                d2[t[i]] = q + 1
            else:
                d2[t[i]] = 1
        
        return d1 == d2
