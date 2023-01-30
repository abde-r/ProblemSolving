class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = ['']
        mx = 0
        for i in arr:
            for j in res:
                s = j+i
                if len(s) != len(set(s)):
                    continue
                res.append(s)
                mx = max(mx, len(s))
        return mx

