def decr(x):
    for i in range(x, -1, -1):
        yield i
a = decr(x = int(input()))
for i in a:
    print(i)