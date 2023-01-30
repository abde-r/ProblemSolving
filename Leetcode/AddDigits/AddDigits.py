class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            sum = 0
            for d in str(num):
                sum += int(d)
            num = sum
        return num

