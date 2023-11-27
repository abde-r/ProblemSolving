def solution(picture):
    
    t=[]
    s='*'*(len(picture[0])+2)
    t.append(s)
    for i in picture: t.append('*'+i+'*')
    t.append(s)
    return t
