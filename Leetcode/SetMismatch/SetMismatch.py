class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        missin = 0
        # getting the value of the missing number
        for i in range(min(nums), max(nums)+1):
            if i not in nums:
                missin = i
                break
        # checking if the missing value is beyond the limits of max and min of nums then assign it properly
        if not missin:
            if min(nums) == 1:
                missin = max(nums)+1
            else:
                missin = 1
        i = 0
        # getting the index of duplicate number
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                return [nums[i],missin]
            i+=1

