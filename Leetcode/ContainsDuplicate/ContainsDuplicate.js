var containsDuplicate = function(nums) {
    nums.sort()
    let i=0
    while (i<nums.length-1)
    {
        if (nums[i] == nums[i+1])
            return true
        i+=1
    }
    return false
};

