import re
s = input()
x = re.search("ab*", s)
if x :
    print(x.string)
else:
    print("None")