class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        t= []
        for i in nums:
            t.append(abs(i))
        if min(t) not in nums:
            return min(t)*-1
        return min(t)
    
