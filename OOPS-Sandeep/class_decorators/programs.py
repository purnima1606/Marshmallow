# attaching init method to a class through class decorator

def demo(self, name):
    self.name = name


def attach(cls):
    cls.__init__ = demo        # Greet.__init__ = demo
    return cls


@attach         # Greet = attach(Greet)
class Greet:

    def greeting(self):
        print(f"Hello {self.name}")

f = Greet("John")   # eventhough there is no __init__ in class Greet, it has been attached through
# the class decorator

#######################################################################################################

prices = {"iphone": 800, "imac": 2500, "iwatch": 300}

def attach_prices(cls):
    cls.prices = prices
    return cls

@attach_prices        # ShoppingCart = attach_(ShoppingCart)
class ShoppingCart:

    def demo(self):
        print(ShoppingCart.prices)

#######################################################################################################
def add(self, a, b):
    return a + b

def sub(self, a, b):
    return a - b

def mul(self, a, b):
    return a * b

def attach_funcs(cls):
    cls.add = add
    cls.sub = sub
    cls.mul = mul


class Calculator:
    pass

#####################################################################################################
def set_attribute(self, key, value):
    if value < 0:
        raise ValueError("Cannot be negative")
    object.__setattr__(self, key, value)


def intercept(cls):
    cls.__setattr__ = set_attribute
    return cls


class Point(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


#####################################################################################################
# decorating all the functions in the class with the function decorator
def log(func):
    def wrapper(*args, **kwargs):
        print("Logging")
        return func(*args, **kwargs)
    return wrapper


def logging(cls):
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, log(value))       # add = log(add)/ sub = log(sub)/ mul = log(mul)
    return cls

"""
In order to set an attribute to a class outside the class, then the inbuilt function setattr() has to be
used and it internally calls __setattr__ --> similar to len() and __len__
"""

@logging
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b





































