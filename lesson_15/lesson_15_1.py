class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        return self.get_square() == other.get_square()

    def __add__(self, other: object) -> "Rectangle":
        new_rectangle = self.get_square() + other.get_square()

        if new_rectangle == 0:
            return Rectangle(0,0)
        else:
            return Rectangle(new_rectangle, 1)

    def __mul__(self, n: object) -> "Rectangle":
        new_rectangle = self.get_square() * n

        if new_rectangle == 0:
            return Rectangle(0,0)
        else:
            return Rectangle(new_rectangle, 1)

    def __str__(self):
        return f"Довжина:{self.width}, висота:{self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
