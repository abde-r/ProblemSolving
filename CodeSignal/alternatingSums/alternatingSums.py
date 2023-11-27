def solution(a):
    
    l, r=0, 0
    for i in range(len(a)):
        if i%2:
            r+=a[i]
        else:
            l+=a[i]
    return [l,r]
