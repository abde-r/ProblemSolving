class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(' ')
        while "" in t:
            t.remove("")
        return ' '.join(t[::-1])

