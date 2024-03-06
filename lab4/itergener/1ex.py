x = int(input())
gen = (i**2 for i in range(x + 1))
for i in gen:
    print(i)