# super() = Function used in a child class to call methods from a parent class (superclass)
#                   Allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def Description(self):
        print(
            f"It is color {self.color} and {'filled' if self.is_filled else 'not filled'}"
        )


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def Description(self):
        print(f"It is a circle with an area of {3.14 *self.radius * self.radius / 2}cm^2")
        super().Description()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def Description(self):
        print(f"It is a Square with an area of {self.width * self.width}cm^2")
        super().Description()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def Description(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().Description()


circle = Circle("blue", True, 20)
circle.Description()
print()

Square = Square("yellow", False, 15)
Square.Description()
print()

triangle = Triangle("red", True, 10, 10)
triangle.Description()
print()
