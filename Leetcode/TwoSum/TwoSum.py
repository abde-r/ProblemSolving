class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums[len(nums) - 1] + nums[len(nums) -2] == target:
            t = [len(nums) - 1, len(nums) - 2]
            return (t)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    t = [i,j]
                    return (t)

