var majorityElement = function(nums) {
    let t = {}

    for (j in nums) t[nums[j]] ? t[nums[j]].count++ : t[nums[j]] = 
    { val: nums[j], count: 1 };

    let r = Object.values(t).sort(function(a,b) 
    { return b.count - a.count }).map(({ val }) => val);

    return r[0]
};

