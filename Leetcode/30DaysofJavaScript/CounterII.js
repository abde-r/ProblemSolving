var createCounter = function(init) {
    let temp = init
    return {
        increment : () => {
            return ++temp
        },
        decrement : () => {
            return --temp
        },
        reset : () => {
            return temp = init
        }
    }
};

