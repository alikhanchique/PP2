def hist(lst, n):
    for i in lst:
        p = i
        print(end = "\n")
        while p > 0:
            p -= 1
            print("*", end = "")


n = int(input())
lst = []
for i in range(0, n):
    e = int(input())
    lst.append(e)
hist(lst, n)
