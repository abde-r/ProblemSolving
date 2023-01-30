class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        s.replace(' ','')
        for x in s:
            if x.isalnum():
                t.append(x)
        if (''.join(t)).lower()[::-1]==(''.join(t)).lower():
            return True
        return False

