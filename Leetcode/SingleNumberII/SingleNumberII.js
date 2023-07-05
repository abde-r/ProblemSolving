 function sortByOccurrences(list) {
  const frequencyMap = new Map();
  for (let element of list)
    frequencyMap.set(element, (frequencyMap.get(element) || 0) + 1);
  
  list.sort((a, b) => {
    const countA = frequencyMap.get(a);
    const countB = frequencyMap.get(b);
    if (countA === countB)
      return a - b;
    else
      return countB - countA;
  });
  return list;
}

var singleNumber = function(nums) {
  r = sortByOccurrences(nums)
  return r[r.length-1]
};

