var sortArrayByParity = function(nums) {
    let len = nums.length
    for (let i=0; i<len; i++)
    {
        if (nums[i]%2 == 0)
        {
            nums.unshift(nums[i])
            nums.splice(i+1, 1)
        }
    }
    return nums
};

