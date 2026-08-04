class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        i = j = 0
        l = len(s)
        max_l = 0
        while(i < l and j < l):
            if s[j] in sub:
                sub.remove(s[i])
                i += 1
            else:
                sub.add(s[j])
                j += 1
            max_l = max(max_l, len(sub))

        return max_l


        