class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        r = []

        for s in strs:
            p = ''.join(sorted(s))
            l = d.get(p, None)

            if(l == None):
                d[p] = [s]
            else:
                l.append(s)
                d[p] = l
        
        for key, value in d.items():
            r.append(value)


        return r


        