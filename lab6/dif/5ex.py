l = []
n = int(input())
for i in range(0, n):
    e = input()
    l.append(e)
 
# writ to file
file = open('myfile.txt', 'w')
file.writelines(l)
file.close()