import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
r = float(input("Enter the radius of the circle: "))
my_circle = Circle(r)
print("Area of the circle is:", my_circle.area())
print("Perimeter of the circle is:", my_circle.perimeter())
