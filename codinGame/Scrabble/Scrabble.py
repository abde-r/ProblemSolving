Points = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

t = []

n = int(input())

for i in range (0,n):
    s = input()
    t.append(s)

letters = input()

r = ''
count = 0
for x in t:
    temp = 0
    w = list(letters)
    for y in x:
        if y in w:
            temp+=Points[y]
            try:
                w.remove(y)
            except:
                temp = -1
                break
        else:
            temp =-1
            break
    if temp > count:
        count = temp
        r = x

print(r)

