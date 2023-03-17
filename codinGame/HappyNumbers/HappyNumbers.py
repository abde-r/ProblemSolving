n = int(input())

for i in range(n):
    x = int(input())
    o=x
    s=0
    count=0
    while x>=1:
        s=0
        for r in str(x):
            s+=int(r)**2
        x=s
        if x==1:
            print(o, ':)')
            break
        if count>20:
            print(o, ':(')
            break
        count+=1

