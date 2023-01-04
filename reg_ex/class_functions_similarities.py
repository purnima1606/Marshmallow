# passing different types of arguments to class
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b


# passing positional arguments
p1 = Point(1, 2)    # Point.__init__(p1, 3, 4)
p2 = Point(3, 4)    # Point.__init__(p2, 3, 4)

# passing keyword arguments
p3 = Point(a=5, b=6)    # Point.__init__(p3, 5, 6)

######################################################################
# creating default parameter / overloaded constructor
class Point:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c


p1 = Point()    # Point.__init__(p1, 0, 0, 0)
p2 = Point(1)    # Point.__init__(p2, 1, 0, 0)
p3 = Point(5, 6)    # Point.__init__(p3, 5, 6, 0)
p4 = Point(1, 2, 3)     # Point.__init__(p4, 1, 2, 3)

"""
overloaded constructor in java

class Point:
    Point():
        this.Point(0, 0, 0)
    Point(a):
        this.Point(a, 0, 0)
    Point(a, b):
        this.Point(a, b, 0)
    Point(a, b, c):
        this.Point(a, b, c)
"""

###########################################################################
""" ********* constructor overriding **********
multiple constructor in the same class leads to 
overriding of constructor and only the latest one will be considered.
"""
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


""" In the above example only the init() with 3 arguments will be considered
and it is not possible to access the init() with 2 arguments"""

