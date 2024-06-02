import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f"Rectangle: area={rectangle.area()}, perimeter={rectangle.perimeter()}")

print(f"Circle: area={round(circle.area(), 2)}, perimeter={round(circle.perimeter(), 2)}")

