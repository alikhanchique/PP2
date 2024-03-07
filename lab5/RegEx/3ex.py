import re
s = input()
x = re.search('^[a-z]+_[a-z]+$', s)
if x:
    print(x.string)
else:
    print("nONE")