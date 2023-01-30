class Solution:

    def guessNumber(self, n: int) -> int:
        r=1
        while r<=n:
            x = (n+r)//2
            g = guess(x)
            if g == 0:
                return x
            elif g>0:
                r = x+1
            elif g<0:
                n = x-1

