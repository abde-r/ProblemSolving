def solution(inputString):
    
    s = list(filter(None, inputString.split('.')))
    if len(s)==4 and inputString.count('.')==3:
        for i in s:
            if not i.isnumeric() or int(i)<0 or int(i)>255 or (len(i)>1 and i[0]=='0'):
                return False
        return True
    return False
