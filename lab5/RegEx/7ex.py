import re
def s_to_c(word):
    y = []
    for i in word.split('_'):
        v = ''.join(i.capitalize())
        y.append(v)
    return ''.join(y)
s = input()
print(s_to_c(s))