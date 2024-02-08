class Prime:
    def __init__(self, n):
        self.lst = []
        self.n = n
    def filter(self):
        self.u = []
        for i in range(0, n):
            self.e= int(input())
            self.lst.append(self.e)
        for i in self.lst:
            self.p = i
            if self.Prime():
                self.u.append(self.p)
        print(self.u)
    def Prime(self):
        self.x =  all([(self.p%j) for j in range(2, int(self.p**0.5) + 1)]) and self.p > 1
        return self.x
n = int(input())
c = Prime(n)
c.filter()


