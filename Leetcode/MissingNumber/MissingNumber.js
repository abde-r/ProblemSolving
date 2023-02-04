var missingNumber = function(nums) {
    let i
    nums.sort(function(a, b) {return a-b})
    for (i=0; i < nums.length; i++)
        if (nums[i] != i)
            return i
    return i
};

