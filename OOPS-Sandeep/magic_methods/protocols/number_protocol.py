class Points:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):   # should return same object after adding
        x = self.a + other.a
        y = self.b + other.b
        return Points(x, y)

    def __sub__(self, other):   # should return same object after subtracting
        x = self.a - other.a
        y = self.b - other.b
        return Points(x, y)

    def __mul__(self, other):   # should return same object after multiplying
        x = self.a * other.a
        y = self.b * other.b
        return Points(x, y)


p1 = Points(1, 2)
p2 = Points(3, 4)
print(p1 + p2)  # point object
print(p1 - p2)  # point object
print(p1 * p2)  # point object
