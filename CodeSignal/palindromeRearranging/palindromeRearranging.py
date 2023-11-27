def solution(inputString):
    
    s = ''.join(sorted(list(set(inputString))))
    count=0
    for i in s:
        if inputString.count(i)%2: count+=1
        if count>1: return False

    return True
