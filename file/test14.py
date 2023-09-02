class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("here is the area!")

class Triangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        super().area()
        print(f"the area of {self.name} is {self.width * self.height}")

my_triangle = Triangle("My Triangle", 5, 5)
my_triangle.area()







