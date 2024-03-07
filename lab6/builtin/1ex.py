import math
n = int(input())
l = []
s = 1
for i in range(0, n):
    ele = int(input())
    l.append(ele)
r = math.prod(l)
print(r)