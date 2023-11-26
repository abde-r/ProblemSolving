def solution(inputArray):
    t = []
    for i in range(1, len(inputArray)):
        t.append(inputArray[i]*inputArray[i-1])
    return max(t)