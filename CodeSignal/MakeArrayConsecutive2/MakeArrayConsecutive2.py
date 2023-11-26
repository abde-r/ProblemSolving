def solution(statues):
    return max(statues)-min(statues)+1 - len(statues)
