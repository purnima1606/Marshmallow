# Checking if the value to be set is validated or not
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setitem__(self, index, value):
        if index == 0:
            if value in range(0, 101):
                self.a = value
            else:
                raise Exception("Allowed range for 'a' is 0 to 100")
        elif index == 1:
            if value in range(0, 51):
                self.b = value
            else:
                raise Exception("Allowed range for 'b' is 0 to 50")
        else:
            raise IndexError

"""
The problem here is that the values passed to the constructor will not be passed
through __setitem__ so those values passed to constructor cannot be controlled.
"""

p = Point(-1, 100)  # values will be set to a and b even they are invalid
print(p.a)
print(p.b)
p[0] = -1   # throws Error as it passes through __setitem__
p.a = -1    # doesnot throw any exception as it doesnot pass through __setitem__,
            # but it passes through __setattr__ method by default

##############################################################################


