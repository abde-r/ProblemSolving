var my_reverse = function(nums, start, end)
{
    let temp
    while (start < end)
    {
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start++
        end--
    }
}

var rotate = function(nums, k) {
    k = k%nums.length
    
    my_reverse(nums, 0, nums.length-1)
    my_reverse(nums, 0, k-1)
    my_reverse(nums, k, nums.length-1) 
};

