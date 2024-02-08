class Shape:
    def __init__(self):
        self.length = 0
    def area(self):
        print(self.length)

class Rectangle:
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.width = int(input())
    def area(self):
        print(self.length*self.width)

            

x = Rectangle(int(input()))
x.area()
