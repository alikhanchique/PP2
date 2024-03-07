import re
s = input()
x = re.search("ab{2,3}", s)
if x:
    print(x)
else:
    print("None")