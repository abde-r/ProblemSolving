class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split(' ')
        for i in range(len(r)):
            r[i] = r[i][::-1]
        return ' '.join(r)

