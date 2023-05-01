var average = function(salary) {
    salary = salary.filter(number => number !== Math.max(...salary))
    salary = salary.filter(number => number !== Math.min(...salary))
    return salary.reduce((x,y) => x+y)/salary.length
};

