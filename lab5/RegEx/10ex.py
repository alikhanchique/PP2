import re
s = input()
x1 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s)
print(x1.lower())

