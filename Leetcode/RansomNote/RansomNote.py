class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        t = []
        t[:0] = magazine
        for i in ransomNote:
            if i not in t:
                return False
            t.remove(i)
        return True

