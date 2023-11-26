def solution(inputString):
    for i in range(len(inputString)//2):
        if inputString[i] != inputString[len(inputString)-i-1]:
            return False;
    return True;
        

