class Shape:
    def __init__(self):
        self.length = 0
    def area(self):
        print(self.length)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length**2)

x = Square(int(input()))

x.area()
