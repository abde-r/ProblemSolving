var findNumberOfLIS = function(nums) {
    let n = nums.length

    let t = new Array(n).fill(1)
    let counts = new Array(n).fill(1)

    for (let i = 0; i < n; i++)
    {
        for (let j = 0; j < i; j++)
        {
            if (nums[i] > nums[j])
            {
                if (t[j] + 1 > t[i])
                {
                    t[i] = t[j] + 1
                    counts[i] = counts[j]
                }
                else if (t[j] + 1 === t[i])
                    counts[i] += counts[j]
            }
        }
    }

    let _max = 0
    for (let i = 0; i < n; i++)
        _max = Math.max(_max, t[i])

    let r = 0;
    for (let i = 0; i < n; i++)
        if (t[i] === _max)
            r += counts[i]

    return r
};

