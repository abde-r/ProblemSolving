def solution(inputArray):
    
    x_obs = sorted(inputArray)
    k=True
    j=1
    
    while k:
        k=False
        j+=1
        for i in range(len(x_obs)):
            if not x_obs[i]%j:
                k=True
                break
    return j
        
