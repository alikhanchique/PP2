import math
def vol(r):
    v = (4/3) * math.pi *(r**3) 
    return v
r = int(input())
print(vol(r))