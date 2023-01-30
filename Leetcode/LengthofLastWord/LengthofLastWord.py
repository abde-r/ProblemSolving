class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split()
        return len(t[len(t)-1])

