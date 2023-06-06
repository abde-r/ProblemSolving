var canMakeArithmeticProgression = function(arr) {
    if (arr.length)
    {
        arr.sort((a, b) => {return a-b})
        diff = Math.abs(arr[1]-arr[0])
        
        for (let i=1; i<arr.length; i++)
            if (Math.abs(arr[i] - arr[i-1]) != diff)
                return false
        return true
    }
};

