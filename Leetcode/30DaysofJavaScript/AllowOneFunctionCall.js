var once = function(fn) {
    let lock = true
    return function(...args){
        if (lock)
        {
            lock = false
            return fn(...args)
        }
        else
            return undefined
    }
};

