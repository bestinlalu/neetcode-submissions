class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dial = { '2' : ['a', 'b', 'c'], 
                 '3' : ['d', 'e', 'f'],
                 '4' : ['g', 'h', 'i'],
                 '5' : ['j', 'k', 'l'],
                 '6' : ['m', 'n', 'o'],
                 '7' : ['p', 'q', 'r', 's'],
                 '8' : ['t', 'u', 'v'],
                 '9' : ['w', 'x', 'y', 'z'] }

        res, self.subset = [], ''

        def dfs(idx):
            if idx >= len(digits):
                res.append(self.subset)
                return
            for letter in dial[digits[idx]]:
                self.subset += letter
                dfs(idx + 1)
                self.subset = self.subset[ : -1]

        dfs(0)
        return res