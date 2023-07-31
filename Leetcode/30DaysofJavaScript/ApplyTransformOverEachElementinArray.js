var map = function(arr, fn) {
    let r=[]
    for (let i=0; i<arr.length; i++)
        r[i] = fn(arr[i], i)
    return r
};

