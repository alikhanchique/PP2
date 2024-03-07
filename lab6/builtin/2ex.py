s = input()
u = 0
l = 0
for c in s:
    if c.isupper():
        u += 1
    elif c.islower():
        l += 1
t = "there are {} upper, and {} lower"
print(t.format(u , l))