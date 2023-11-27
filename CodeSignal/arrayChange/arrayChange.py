def solution(inputArray):
    
    count=0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            if inputArray[i-1]<0:
                count+=abs(inputArray[i-1]-inputArray[i])+1
                inputArray[i]=inputArray[i-1]+1
            else:
                count+=inputArray[i-1]+1-inputArray[i]
                inputArray[i]=inputArray[i-1]+1
    return count
