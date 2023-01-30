class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        j=0
        if len(strs) == 1 and not strs[0]:
            return ""
        if len(strs) == 1:
            return strs[0]
        g = min(strs, key=len)
        index = strs.index(g)
        while i<len(strs[index]):
            temp = strs[index][i]
            j = 0
            while j < len(strs):
                if strs[j][i] != temp:
                    return strs[index][:i]
                j+=1
            i+=1
        return strs[index][:i]

