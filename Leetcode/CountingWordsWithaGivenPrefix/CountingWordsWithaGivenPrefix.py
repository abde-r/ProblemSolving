class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        x = 0
        for i in words:
            if pref in i:
                if i[0:len(pref)] == pref:
                    x+=1
        return x

