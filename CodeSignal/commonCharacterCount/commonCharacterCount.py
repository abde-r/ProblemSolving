def solution(s1, s2):
    
    i, count, c, g=0, 0, 0, len(s1)
    
    while len(s1)>0 and len(s2)>0 and c<g:
        if s1[i] in s2:
            s2 = s2.replace(s2[s2.find(s1[i])], '', 1)
            s1 = s1.replace(s1[i], '', 1)
            count+=1
        else:
            i+=1
        c+=1
    return count
