x = int(input())
gen = (i for i in range(0, x+1) if i%3==0 or i%4==0)
lst = []
for i in gen:
    lst.append(i)
print(*lst, sep=', ')

