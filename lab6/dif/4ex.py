with open(r"myfile.txt" , 'r') as f:
    l = len(f.readlines())
print(l)