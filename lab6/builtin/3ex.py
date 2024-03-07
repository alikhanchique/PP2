def Pali(s):
    r = ''.join(reversed(s))
    if (s == r):
        return True
    return False
s = input()
x = Pali(s)
 
if (x):
    print("Yes")
else:
    print("No")