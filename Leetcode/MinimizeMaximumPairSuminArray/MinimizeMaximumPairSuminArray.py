class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        nums = sorted(nums)
        temp = nums[0]+nums[j]
        while i < j:
            if nums[i]+nums[j]>temp:
                temp = nums[i]+nums[j]
            j-=1
            i+=1
        return temp

