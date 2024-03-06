def Squares(a, b):
    for i in range(a, b+1):
        yield i**2

x = Squares(a = int(input()), b = int(input()))
for i in x:
    print(i)