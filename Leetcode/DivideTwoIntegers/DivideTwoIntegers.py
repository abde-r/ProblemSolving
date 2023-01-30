class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = dividend/divisor
        if r>2147483647:
            return 2147483647
        return int(r)

