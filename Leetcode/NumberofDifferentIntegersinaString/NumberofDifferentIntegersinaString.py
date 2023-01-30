class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        i=0
        t = []
        while i < len(word):
            j=i
            while i < len(word) and ord(word[i]) >= 48 and ord(word[i]) <= 57:
                i+=1
            t.append(word[j:i])
            i+=1
        while "" in t:
            t.remove("")
        s = []
        for n in t:
            s.append(int(n))
        r = set(s)
        return len(r)

