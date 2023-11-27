def solution(a, b):
    
    if a!=b:
        t1, t2 = [], []    
        for i in range(len(a)):
            if a[i] != b[i]:
                t1.append(a[i])
                t2.append(b[i])
        
        if len(t1) != 2 or t1 != t2[::-1]:
            return False
    return True
