class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i=0
        sorted(nums)
        while i in nums:
            if not i:
                nums.remove(i)
        nums = set(nums)
        return len(nums)

