class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __bool__(self):
        if self.a == 0 or self.b == 0:
            return False
        return True


p1 = Point(1, 2)

if p1:
    print("Has some valid co-ordinates")
else:
    print("Both co-ordinates are zero")


"""
- If __bool__() is not implemented in any class(eg. list), then python checks 
  for __len__() as a fallback(back up) method and checks for its return value
  as it is an integer. If the value is 0 --> False else True

- If both __bool__() and __len__() are not implemented in a class, then its 
  object will always evaluates to boolean True else it depends on the 
  implementation written in  __bool__().

"""
