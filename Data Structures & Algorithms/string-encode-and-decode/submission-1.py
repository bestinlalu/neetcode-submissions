class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st = st + str(len(s)) + "#" + s
        print(st)
        return st

    def decode(self, s: str) -> List[str]:

        strs = []
        d = i = 0

        while(i < len(s)):
            if s[i] != '#':
                d = d * 10 + int(s[i])
                i += 1
                continue
            print(s[i + 1 : i + d + 1])
            strs.append(s[i + 1 : i + d + 1])
            i += d + 1
            d = 0
            print(i)

        return strs
