var nextGreatestLetter = function(letters, target) {
    letters.sort()
    let i=0
    while (letters[i] <= target)
        i++
    if (i < letters.length)
        return letters[i]
    return letters[0]
};

