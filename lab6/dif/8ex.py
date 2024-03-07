import os

file = input()
print(os.path.isfile(file))
location = input()

path = os.path.join(location, file)

os.remove(path)