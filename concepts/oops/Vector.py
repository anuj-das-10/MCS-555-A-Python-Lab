class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __gt__(self, other):
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)

# Example usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# String representation
print(str(v1))  # Output: Vector(3, 4)

# Addition
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

# Subtraction
v4 = v1 - v2
print(v4)  # Output: Vector(2, 2)

# Multiplication by scalar
v5 = v1 * 3
print(v5)  # Output: Vector(9, 12)

# Comparison
print(v1 > v2)  # Output: True
print(v1 < v2)  # Output: False
