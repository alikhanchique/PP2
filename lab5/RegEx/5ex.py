import re
s= input()
x = re.search('a.*?b$', s)
if x:
    print(x.string)
else:
    print("None")
