var cancellable = function(fn, args, t) {
    let timeOut = setTimeout(() =>
        fn(...args)
    , t)

    let cancelFn = () => clearTimeout(timeOut)
    return cancelFn
};

