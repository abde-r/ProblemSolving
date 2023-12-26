def solution(matrix):
    
    t=[]
    for i in range(len(matrix)):
        t.append([])
        for j in range(len(matrix[i])):
            count=0
            if j-1>=0 and matrix[i][j-1]:
                count+=1
            if j+1<len(matrix[i]) and matrix[i][j+1]:
                count+=1
                
            if i-1>=0:
                if matrix[i-1][j]:
                    count+=1
                if j-1>=0 and matrix[i-1][j-1]:
                    count+=1
                if j+1<len(matrix[i]) and matrix[i-1][j+1]:
                    count+=1
                
            if i+1<len(matrix):
                if matrix[i+1][j]:
                    count+=1
                if j-1>=0 and matrix[i+1][j-1]:
                    count+=1
                if j+1<len(matrix[i]) and matrix[i+1][j+1]:
                    count+=1
            t[i].append(count)
    return t
