class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        d = [0] * 26
        t = [0] * 26
        for c in s1:
            d[ord(c) - ord('a')] += 1
        k = 0
        i = 0
        j = len(s1)
        while(k < len(s1)):
            t[ord(s2[k]) - ord('a')] += 1
            k += 1
        print(str(t))
        print(str(d))
        if(str(d) == str(t)):
            return True
        while(j < len(s2)):
            t[ord(s2[i]) - ord('a')] -= 1
            t[ord(s2[j]) - ord('a')] += 1
            print(str(t), s2[i:j + 1])
            print(str(d))
            if(str(t) == str(d)):
                
                return True
            j += 1
            i += 1

        return False
            

