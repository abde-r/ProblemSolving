def solution(a):
    
    t = []
    for i in a:
        if i!=-1: t.append(i)
    t.sort(reverse=True)
    
    for i in range(len(a)):
        if a[i]!=-1: a[i] = t.pop()
    return a
