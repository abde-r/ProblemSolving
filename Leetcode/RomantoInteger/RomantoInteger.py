class Solution:
    def romanToInt(self, s: str) -> int:
        dictio = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        i = 0
        while i<len(s):
            if s[i] in dictio:
                if s[i] == 'I':
                    if i+1<len(s) and s[i+1] == 'V':
                        res += 4
                        i+=1
                    elif i+1<len(s) and s[i+1] == 'X':
                        res += 9
                        i+=1
                    else:
                        res += dictio[s[i]]
                elif s[i] == 'X':
                    if i+1<len(s) and s[i+1] == 'L':
                        res += 40
                        i+=1
                    elif i+1<len(s) and s[i+1] == 'C':
                        res += 90
                        i+=1
                    else:
                        res += dictio[s[i]]
                elif s[i] == 'C':
                    if i+1<len(s) and s[i+1] == 'D':
                        res += 400
                        i+=1
                    elif i+1<len(s) and s[i+1] == 'M':
                        res += 900
                        i+=1
                    else:
                        res += dictio[s[i]]
                else:
                    res += dictio[s[i]]
                i+=1
        return res

