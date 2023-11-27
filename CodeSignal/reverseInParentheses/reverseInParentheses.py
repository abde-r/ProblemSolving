import re

def solution(inputString):

    firstIndex = inputString.rfind('(')
    lastIndex = inputString.find(')', firstIndex)
    while firstIndex != -1:
        inputString = inputString[:firstIndex]+inputString[firstIndex+1:lastIndex][::-1]+inputString[lastIndex+1:]
        firstIndex = inputString.rfind('(')
        lastIndex = inputString.find(')', firstIndex)
    
    return inputString
        
