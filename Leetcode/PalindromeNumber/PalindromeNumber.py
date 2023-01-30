class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x>2147483647:
            return False
        t = [int(i) for i in str(x)]
        for i in range(0, len(t)//2):
            if t[i] != t[len(t)-1-i]:
                return False
        return True

