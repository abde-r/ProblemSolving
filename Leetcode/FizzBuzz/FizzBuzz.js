var fizzBuzz = function(n) {
    let t = []
    for (i=1; i<=n; i++)
    {
        if (i%3 == 0 && i%5 == 0)
            t.push('FizzBuzz')
        else if (i%3 == 0)
            t.push('Fizz')
        else if (i%5 == 0)
            t.push('Buzz')
        else
            t.push(i.toString())
    }
    return t
};

