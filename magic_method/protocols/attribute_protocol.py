# Accessing attributes using dot operator/ performing attribute look up in a class
"""
In order to access any value inside a class using indexing __getitem__ and
__setitem__ should be present
"""


class PositivePoint:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __getattribute__(self, item):   # for every attribute access it will be triggered
    #     print(f"Getting: {item}")
    #     return super().__getattribute__(item)

    def __setattr__(self, name, value):  # for every attribute assignment it will get triggered
        if value < 0:
            raise Exception("value must be positive")

        print(f"Setting: {name} to {value}")
        super().__setattr__(name, value)    # __setattr__ of object class


# p = PositivePoint(1, 2)
# print(p.a)      # __getattribute__ of object class
# p.a = 12        # __setattr__

"""
Even though __getattribute__ and __setattr__ is not present explicitly in class Points,
they will be applied by default as they are inherited from Object class.
"""


#############################################################################
# overriding __setattr__ of object class in child classes
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        # setting uppercase of the input string
        super().__setattr__(name, value.upper())

###########################################################################
class  Sample:

    def __init__(self, dict_):
        self.d = dict_      # self - {d: {"a": 1, "b": 2}}

    def __getitem__(self, item):
        return self.d[item]

    def __getattribute__(self, item):
        return self.d[item]

    def __getattr__(self, item):    # it is used to access the missing attributes
        return self.d[item]


d = {"a": 1, "b": 2}

s = Sample(d)
print(s["a"])
print(s.a)












