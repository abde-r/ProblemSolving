expression = input()

s = expression.split(' + ')

units = {
    'um': 1000000000,
    'mm' : 1000000,
    'cm' : 100000,
    'dm' : 10000,
    'm' : 1000,
    'km' : 1
}

if s[0][len(s[0])-2:].isalpha() and s[0][len(s[0])-1:].isalpha():
    uni1 = s[0][len(s[0])-2:]
else:
    uni1 = s[0][len(s[0])-1:]

if s[1][len(s[1])-2:].isalpha() and s[1][len(s[1])-1:].isalpha():
    uni2 = s[1][len(s[1])-2:]
else:
    uni2 = s[1][len(s[1])-1:]

if uni1>uni2:
    m=1
elif uni1<uni2:
    m=0
else:
    m=2

if s[0][len(s[0])-2:].isalpha() and s[0][len(s[0])-1:].isalpha():
    if '.' in s[0]:
        n1 = float(s[0][:len(s[0])-2])
    else:
        n1 = int(s[0][:len(s[0])-2])
else:
    if '.' in s[0]:
        n1 = float(s[0][:len(s[0])-1])
    else:
        n1 = int(s[0][:len(s[0])-1])

if s[1][len(s[1])-2:].isalpha() and s[1][len(s[1])-1:].isalpha():
    if '.' in s[1]:
        n2 = float(s[1][:len(s[1])-2])
    else:
        n2 = int(s[1][:len(s[1])-2])
else:
    if '.' in s[1]:
        n2 = float(s[1][:len(s[1])-1])
    else:
        n2 = int(s[1][:len(s[1])-1])

if m==1:
    rn = (units[uni2]*n1)/units[uni1]
    print(round(rn+n2), end='')
elif m==0:
    rn = (n1*units[uni2])/units[uni1]
    s = str(rn)
    g = 0
    for i in range(s.index('.')+1, len(s)):
        if s[i] != '0':
            g+=1
    if g == 0:
        print(round(rn)+n2, end='')
    else:
        print(rn+n2, end='')
else:
    print(n1+n2,end='')
print(uni2)

