x = int(input())
gen = (i for i in range(x+1) if i%2==0)
lst = [gen]
for i in lst:
    print(i)