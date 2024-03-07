import re
s = input()
x= re.sub("[ , .]", ":", s)
if x:

    print(x)
else:
    print("None")