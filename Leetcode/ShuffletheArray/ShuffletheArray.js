var shuffle = function(nums, n) {
    let t = []
    for (let i=0; i<n; i++)
    {
        t.push(nums[i])
        t.push(nums[i+n])
    }
    return t
};

