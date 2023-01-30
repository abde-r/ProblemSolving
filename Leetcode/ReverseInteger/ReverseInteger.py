class Solution:
    def reverse(self, x: int) -> int:
        sig = 1
        if x<-2147483648 or x>2147483647:
            return 0
        if x<0:
            sig *= -1
            s = str(abs(x))
        else:
            s = str(x)
        x = int(s[::-1])*sig
        if x<-2147483648 or x>2147483647:
            return 0
        return x

