w, h = [int(i) for i in input().split()]
t = []
for i in range(h):
    for j in input().split():
        pixel = int(j)
        t.append(bin(pixel)[len(str(bin(pixel)))-1])
r=''
c=0
s=''
for i in t:
    if c==8:
        c=0
        s+=chr(int(r[:8], 2))
        r=''
    r+=str(i)
    c+=1
if r != '':
    s+=chr(int(r[:8], 2))
print(s)

