class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n,d= sum(nums),0
        for i in nums:
            for x in str(i):
                d += int(x)
        return n-d

