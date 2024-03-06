import math
n = int(input())
l = int(input())
r = n*l
a = int(r/(4 * math.tan(math.pi/n)))
print(a**2)