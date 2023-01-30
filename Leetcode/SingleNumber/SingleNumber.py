import numpy as np

class Solution: 
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums):
            temp = i
            if (i+1) < len(nums):
                i+=1
            else:
                return nums[temp]
            while nums[i] == nums[temp] and i < len(nums):
                i = i+1
            if i == (temp+1):
                return nums[temp]

