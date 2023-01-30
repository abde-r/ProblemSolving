class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        i = 0
        while i < len(s):
            i+=1
        if i==26:
            return True
        return False

