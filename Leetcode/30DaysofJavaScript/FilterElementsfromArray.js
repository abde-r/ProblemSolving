var filter = function(arr, fn) {
    let r=[]
    for (let i=0; i<arr.length; i++)
        if (fn(arr[i], i))
            r.push(arr[i])
    return r
};

