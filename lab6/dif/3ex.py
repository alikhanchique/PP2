import os
path = input()
print(os.path.exists(path))
print("\nFilename of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))