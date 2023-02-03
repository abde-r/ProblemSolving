var findTheDifference = function(s, t) {
    s = s.split('').sort().join()
    t = t.split('').sort().join()
    for (let i=0; i<s.length; i++)
    {
        if (t[i] != s[i])
            return t[i]
    }
    return t[t.length-1]
};

