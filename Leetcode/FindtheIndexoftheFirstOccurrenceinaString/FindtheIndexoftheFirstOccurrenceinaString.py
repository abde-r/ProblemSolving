class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = haystack.find(needle)
        if n<0:
            return -1
        return n

