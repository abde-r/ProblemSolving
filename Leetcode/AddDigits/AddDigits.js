var addDigits = function(num) {
    let r=num
    while (r.toString().length > 1)
    {
        let s = num.toString().split('')
        r=0
        for (let i=0; i<s.length; i++)
            r+=Number(s[i])
        num = r
    }
    return r
}

