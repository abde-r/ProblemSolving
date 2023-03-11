import sys
import math

n = int(input())
q = int(input())

dictio = {
    ext.lower(): mt for ext, mt in (input().split() for _ in range(n))
}

fnames = [input() for i in range(q)]

for i in fnames:
    if '.' not in i:
        print("UNKNOWN")
    else:
        _, s = i.rsplit('.', 1)
        print(dictio.get(s.lower(), "UNKNOWN"))

