w = int(input())
h = int(input())
t = input()
r = t.split(' ')

t = []
for i in range(len(r)):
    if not i%2:
        for x in range(int(r[i])):
            t.append('*')
    else:
        for x in range(int(r[i])):
            t.append(' ')

x=0
i=0

while i<len(t):
    if not x:
        print('|', end='')
    if x<w:
        print(t[i], end='')
        x+=1
        i+=1
    else:
        print('|')
        x=0
print('|')

