var isIsomorphic = function(s, t) {
    let x=[], y=[]
    let tempx=[], tempy=[]
    let count=0

    for (let i=0; i<s.length; i++)
    {
        tempx.push(s[i])
        if (!tempx.includes(s[i]))
            count++
        else
            x.push(tempx.indexOf(s[i]))
        tempy.push(t[i])
        if (!tempy.includes(t[i]))
            count++
        else
            y.push(tempy.indexOf(t[i]))
        if (x[i] != y[i])
            return false
    }
    return true
};

