var getCommon = function(nums1, nums2) {
    let t = {}

    for (let i=0; i<nums1.length; i++)
        t[nums1[i]] = 1
    for (let i=0; i<nums2.length; i++)
        if (t[nums2[i]])
            return nums2[i]
    return -1
};

