var kthFactor = function(n, k) {
    const factors = [];
    for (let i = 1; i <= n; i++)
      if (n % i === 0)
          factors.push(i);

    factors.sort((a, b) => a - b);

    if (k <= factors.length)
      return factors[k - 1];
    else
      return -1;
};

