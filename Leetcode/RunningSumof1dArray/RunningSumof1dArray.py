class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t,r = [],0
        for i in nums:
            r+=i
            t.append(r)
        return t

