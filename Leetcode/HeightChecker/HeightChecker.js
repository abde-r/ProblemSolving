var heightChecker = function(heights) {
    let t = []
    let count = 0

    for (let i=0; i<heights.length; i++)
        t.push(heights[i])
    t.sort(function(a,b){return a-b})
    for (let i=0; i<t.length; i++)
        if (heights[i] != t[i])
            count++
    return count
};

