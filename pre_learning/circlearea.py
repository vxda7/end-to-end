class Circle:
    pi=3.14
    def __init__(self, r):
        self.r = r
    
    def area(self):
        print(f"원의 면적: {self.r**2 * self.pi }")

c = Circle(2)
c.area()