def solution(inputString):
    s=''
    for i in range(len(inputString)):
        if (chr((ord(inputString[i])+60)%26+65)).isupper():
            s+=chr((ord(inputString[i])+60)%26+65).lower()
        else:
            s+=chr((ord(inputString[i])+60)%26+65).upper()
    return s
