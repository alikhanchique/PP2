def three(arr, n):
    c = 0
    for i in arr:
        if i == 3:
            c += 1
            if c == 2:
                return True
        else:
            c = 0
    return False
n = int(input())
arr = []
for i in range(0 , n):
    e = int(input())
    arr.append(e)

print(three(arr, n))
