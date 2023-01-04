# implementing summation logic

class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a + self.b < other.a + other.b:
            return True
        return False

    def __gt__(self, other):
        if self.a + self.b > other.a + other.b:
            return True
        return False

    def __eq__(self, other):
        if self.a + self.b == other.a + other.b:
            return True
        return False

    def __ge__(self, other):
        if self.a + self.b >= other.a + other.b:
            return True
        return False

    def __le__(self, other):
        if self.a + self.b <= other.a + other.b:
            return True
        return False

    def __ne__(self, other):
        if self.a + self.b != other.a + other.b:
            return True
        return False


p1 = Point(1, 2)
p2 = Point(3, 4)
# print(p1 < p2)

#######################################################################
# implementing coordinate comparison logic

class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.a and self.b < other.b:
            return True
        return False

    def __gt__(self, other):
        if self.a > other.a and self.b > other.b:
            return True
        return False

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False










