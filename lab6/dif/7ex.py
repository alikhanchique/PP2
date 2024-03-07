with open('a.txt','r') as fir, open('b.txt','w') as sec: 
    for line in fir: 
            sec.write(line)