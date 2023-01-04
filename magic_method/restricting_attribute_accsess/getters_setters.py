# property decorator

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("radius should be float or int")
        self._radius = value    # protected variable

    def circumference(self):
        return 2 * 3.14 * self._radius

#####################################################################################################

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @ property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        if len(value) > 5:
            raise ValueError()
        self._fname = value

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        if len(value) > 5:
            raise ValueError()
        self._lname = value

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if value < 500 and not isinstance(value, (float, int)):
            raise ValueError()
        self._pay = value


#####################################################################################################
"""         
Descriptor Protocol     
1. __get__
2. __set__
3. __del__

Attribute protocol
1. __setattr__
2. __getattribute__
3. __delattr__
"""

######################################################################################################
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError()
        self._a = value     # __setattr__()

    @property
    def b(self):
        return self._b      # __getattribute__()

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError()
        self._b = value

































