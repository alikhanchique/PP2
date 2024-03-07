def alli(tup):
    return all(tup)

u = input("input in row: ")
ut = tuple(map(lambda x: x == 'True', u.split()))
print(alli(ut))