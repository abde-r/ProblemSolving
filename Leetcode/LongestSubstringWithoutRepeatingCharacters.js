var lengthOfLongestSubstring = function(s) {
    let temp=0
    for (let i=0; i<s.length && temp<s.length-i; i++)
    {
        let t = ""
        let j=i
        
        while (!t.includes(s[j]) && j < s.length)
            t+=s[j++]
        if (j-i>=temp)
            temp = j-i
    }
    return temp
};

