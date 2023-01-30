class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        res = 0
        sign = 1
        if not s:
            return 0
        while s[i] == ' ' or s[i] == '\t' or s[i] == '\n' or s[i] == '\r' or s[i] == '\v' or s[i] == '\f':
            i = i+1
            if i==len(s):
                return 0
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            elif s[i] == '+':
                sign = 1
            i=i+1
        if i==len(s):
            return 0
        while ord(s[i])>=48 and ord(s[i])<=57:
            res = res * 10 + ord(s[i]) - 48
            i=i+1
            if i==len(s):
                break
        if res*sign >= 2147483647:
            return 2147483647
        if res*sign <= -2147483648:
            return -2147483648
        return (res * sign)

