var largestNumber = function(nums) {
    t = []
    for (let i=0; i<nums.length; i++)
        t.push(nums[i].toString())
    t.sort((a,b) => { return (b+a) - (a+b) })
    s = t.join('')
    if (s[0] == "0")
        return "0"
    return s
};

