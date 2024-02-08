import math
class Point:
    def __init__(self ,x ,y):
        self.x = x
        self.y = y
    def Show(self):
        self.c = "{}:{}"
        print(self.c.format(self.x ,self.y))     
    def Move(self):
        print("By how much would you like to move points")
        self.a = int(input())
        self.b = int(input())
        c = "{}:{}"
        print(c.format(self.x + self.a, self.y + self.b))  
    def Dist(self):
        print("input coordinates of the second point")
        self.u = int(input())
        self.v = int(input())
        print(math.sqrt((self.u - self.x)**2 + (self.v - self.y)**2))
x = int(input())
y = int(input())
t = Point(x, y)
t.Show()
t.Move()
t.Dist()
