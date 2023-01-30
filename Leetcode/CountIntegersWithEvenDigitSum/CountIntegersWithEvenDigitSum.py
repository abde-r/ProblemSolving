class Solution:
    def countEven(self, num: int) -> int:
        i,r=1,0
        while i<num+1:
            sum=0
            for x in str(i):
                sum+=int(x)
            if not sum%2:
                r+=1
            i+=1
        return r

