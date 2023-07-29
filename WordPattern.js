var wordPattern = function(pattern, s) {
    let x=[], y=[]
    let tempx=[], tempy=[]
    let count=0
    t = s.split(' ')

    for (let i=0; i<t.length; i++)
    {
        tempx.push(t[i])
        if (!tempx.includes(t[i]))
            count++
        else
            x.push(tempx.indexOf(t[i]))
    }

    count = 0
    for (let i=0; i<pattern.length; i++)
    {
        tempy.push(pattern[i])
        if (!tempy.includes(pattern[i]))
            count++
        else
            y.push(tempy.indexOf(pattern[i]))
        if (x[i] != y[i])
            return false
    }

    if (x.length != y.length)
        return false
    console.log(x, y)
    return true
};

