def solution(name):
    
    for i in name:
        if not i.isalnum() and i!='_' or (not name[0].isalpha() and name[0]!='_'):
            return False
    return True
