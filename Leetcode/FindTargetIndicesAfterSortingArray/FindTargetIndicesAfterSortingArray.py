class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        t = []
        x = 0
        for i in nums:
            if i == target:
                t.append(x)
            x+=1
        return t

