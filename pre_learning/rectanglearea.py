class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        print(f"사각형의 면적: {self.x * self.y}")

r = Rectangle(4,5)
r.area()