class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
    
s = Square(10)

print(f"Area of square is {s.area()}")
print(f"Area of square is {s.perimeter()}")