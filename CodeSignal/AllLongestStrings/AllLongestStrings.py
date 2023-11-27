def solution(inputArray):
    
    t = []
    m = len(max(inputArray, key=len))
    for i in inputArray:
        if len(i) == m:
            t.append(i)
    return t
