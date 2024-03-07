import re
s = input()
x = re.search('[A-Z]+[a-z]+$', s)
if x:
    print(x.string)
else:
    print("None")