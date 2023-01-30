class Solution:
    def printVertically(self, s: str) -> List[str]:
        t = s.split(' ')
        temp = sorted(t, key=len, reverse=True)
        i,max_len = 0,len(temp[0])
        r = []
        while i<max_len:
            j=0
            res = ''
            while j<len(t):
                if i<len(t[j]):
                    res+=t[j][i]
                else:
                    res+= ' '
                j+=1
            r.append(res.rstrip())
            i+=1
        return r

