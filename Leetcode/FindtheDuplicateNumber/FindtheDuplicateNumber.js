var findDuplicate = function(nums) {
    let t = []
    for (let i=0; i<nums.length; i++)
    {
        if (!t.includes(nums[i]))
            t.push(nums[i])
        else
            return nums[i]
    }
};

