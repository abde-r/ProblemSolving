var findDifference = function(nums1, nums2) {
    let r = [[],[]]
    for (let i=0; i<nums1.length; i++)
        if (!nums2.includes(nums1[i]) && !r[0].includes(nums1[i]))
            r[0].push(nums1[i])
    for (let i=0; i<nums2.length; i++)
        if (!nums1.includes(nums2[i]) && !r[1].includes(nums2[i]))
            r[1].push(nums2[i])
    return r
};

