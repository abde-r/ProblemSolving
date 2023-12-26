def matrix_sum(t):
    
    count=0
    for i in range(3):
        for j in range(3):
            count+=t[i][j]
    return count//9

def solution(image):
    
    n_rows=len(image)
    n_columns=len(image[0])
    
    m, n = 0, 0
    t, s, b, r=[], [], [], []
    
    while m<=n_rows-3:
        while n<=n_columns-3:
            for i in range(m, m+3):
                for j in range(n, n+3):
                    t.append(image[i][j])
                s.append(t)
                t=[]
            b.append(matrix_sum(s))
            s=[]
            n+=1
        r.append(b)
        b=[]
        m+=1
        n=0
    return r
