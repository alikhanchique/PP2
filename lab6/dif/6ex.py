import string
alp = string.ascii_lowercase
for let in alp:
    with open(let+".txt" , "w") as f:
        f.write(let)