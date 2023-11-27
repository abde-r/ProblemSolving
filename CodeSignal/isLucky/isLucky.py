def solution(n):
    
    l, r=0, 0
    s = str(n)
    if not len(s)%2:
        for i in range(0, len(s)//2): l+=int(s[i])
        for i in range(len(s)//2, len(s)): r+=int(s[i])
        if l==r: return True
    return False
