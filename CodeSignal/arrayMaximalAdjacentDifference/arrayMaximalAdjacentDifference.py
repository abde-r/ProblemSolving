def solution(inputArray):
    
    temp = 0
    for i in range(1, len(inputArray)):
        if abs(inputArray[i]-inputArray[i-1])>=temp:
            temp = abs(inputArray[i]-inputArray[i-1])
    return temp
