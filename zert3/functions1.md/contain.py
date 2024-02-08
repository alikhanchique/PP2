def seven(arr, n):
    c = 0
    for i in arr:
        if c == 2:
            if i == 7:
                return True
        if i == 0:
            c += 1
        else:
            c = 0
    return False
arr = []
n = int(input())
for i in range(0 , n):
    e = int(input())
    arr.append(e)
print(seven(arr, n))
