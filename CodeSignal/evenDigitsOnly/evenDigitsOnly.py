def solution(n):
    
    for i in str(n):
        if int(i)%2:
            return False
    return True
