x = int(input())
gen = (i for i in range(x+1) if i%2==0)
lst = []
for i in gen:
    
    lst.append(i)
print(*lst, sep =', ')