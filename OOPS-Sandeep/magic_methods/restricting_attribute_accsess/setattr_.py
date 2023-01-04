# validating for setting a bad value by redefining __setattr__()
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only int and float are allowed")
        super().__setattr__(name, value)
        # object.__setattr__(self, name, value)

    def mul(self):
        return self.a * self.b


#########################################################################
# raising an exception if the user tries to initialize new value which is not
# present in the __init__

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __setattr__(self, name, value):
        if name not in ["fname", "lname", "pay"]:
            raise ValueError(f"{name} is not an attribute of Employee")
        super().__setattr__(name, value)


#########################################################################
# fname and lname < 5 characters and pay > 500
class Employee:

    def __init__(self, fname, lname, pay):
        # calls __setattr__ of child class i.e., Employee class
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __setattr__(self, name, value):
        if name == "fname" or name == "lname":
            if len(value) > 5:
                raise Exception(f"Length of {name} cannot be > 6")
            super().__setattr__(name, value)

        elif name == "pay":
            if value < 500:
                raise ValueError("Pay should be more than 500")
            super().__setattr__(name, value)
        else:
            raise Exception(f"{name} is not an attribute of Employee class")


############################################################################
# Making a class Immutable i.e., value should not be changed after initialization
# Allowing the user to set the value only once

class Point:

    def __init__(self, a, b):
        # calling __setattr__ of object class directly
        super().__setattr__("a", a)
        super().__setattr__("b", b)

    def __setattr__(self, name, value):
        raise Exception("Point object is immutable")


#########################################################################
class Point:

    def __init__(self, a, b):
        # calling __setattr__ of object class directly
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        super().__setattr__(name, value)



