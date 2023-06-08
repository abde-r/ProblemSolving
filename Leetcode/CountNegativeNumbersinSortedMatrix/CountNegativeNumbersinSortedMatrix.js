var countNegatives = function(grid) {
    let count = 0
    
    for (let i=0; i<grid.length; i++)
        count += grid[i].filter(((x) => x <0 )).length
    return count
};

