class Point:
    # sorting the data
    # constructor / magic method / initializer
    # save the data inside the dictionary, the dictionary is called as instance dictionary....
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reset(self):
        self.a = 0
        self.b = 0

    def move(self, dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy

    def sort(self):
        if self.b < self.a:
            temp = self.a            # low level work
            self.a = self.b
            self.b = temp
            return (self.a, self.b)
        return (self.a, self.b)


p1 = Point(1, 2)
p2 = Point(4, 3)
p3 = Point(5, 6)
print(p1.a)        # 1
print(p1.b)        # 2
# print(Point.a)
# print(Point.b)
# print(p1.__dict__)
# print(p2.__dict__)

# print(p1.reset())
# print(p1.a, p1.b)

# print(p1.move(0.5, 2.3))
# print(p1.__dict__)                        # {'a': 1.5, 'b': 4.3}

# print(p2.move(1.2, 0.7))                  # Point.move(p2, 1.2, 0.7)
# print(p2.__dict__)                        # {'a': 4.2, 'b': 4.7}

# print(p2.sort())      # (3, 4)       # Point.sort(p2)








