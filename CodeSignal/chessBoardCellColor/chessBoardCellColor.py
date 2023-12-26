def solution(cell1, cell2):
    
    s='ABCDEFGH'
    n='12345678'
    if not s.find(cell1[0])%2:
        if s.find(cell2[0])%2:
             if n.find(cell1[1])%2 == n.find(cell2[1])%2:
                return False
        else:
            if n.find(cell1[1])%2 != n.find(cell2[1])%2:
                return False
    else:
        if n.find(cell1[1])%2 != n.find(cell2[1])%2:
                return False
    return True
