class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if str(num)[len(str(num))-1] == '0' and num>9:
            return False
        return True

