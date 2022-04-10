a = [1, 2]
t = (1, 2)
d = {"a": 1, "b": 2}

"""
All variables are pointers in python i.e variables will point to a memory of a 
data and not store the data directly

'a' is of type list
'a' is an instance of class list
'a' is pointing to a list object
"""
############################################################################################
# we can create multiple instances for same class
a1 = [1, 2]
a2 = [3, 4]

t1 = (1, 2)
t2 = (3, 4)

d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "b": 4}

###########################################################################################
# modification done on an object remains in the object only
d1 = {"a": 1, "b": 2}
d2 = {"a": 3, "b": 4}

d1["a"] += 0.5
print(d1)       # d1 = {"a": 1.5, "b": 2}
print(d2)       # d1 = {"a": 3, "b": 4}

###########################################################################################
"""
dir():
* gives the list of operations that can be performed on an instance/object
* these operations are called attributes( variable/property/function/method)
* anything accessed via '.' operator  - attribute
* take some examples of list/tuple/dict to show the methods applied on one object
or instance modifies only that instance.


# *************** magic methods/ special methods ****************

obj.__getitem__(pos) - gives the element in the mentioned position of the instance called
obj.__len__() - given length of the instance called
obj.__contains__(element) - checks if the element is present in the instance called
These above methods act on some data of the given instance

# ************* Attribute look up in a class *******************

- when an attribute is called via an instance, python searches for that attribute 
in the list of attributes of that instance's class
- If the attribute is not implemented in the instance - Attribute Error
- All the attributes are developed in "C"
- In order to achieve some operation on an instance which does not have any 
inbuilt methods in its class, then we need to use low level operations 
like indexing, dictionary look ups
eg:
we don't have swap() in list, in order to swap the data in list, a = [1, 2]
temp = a[0]
a[1] = a[0]
a[0] = temp
"""

# ************************ creating custom classes **************************
# class - container that has set of functions which are used to manipulate the
# data(instance data)

class Point:
    # class data
    x = 10
    y = 20

    # to store data(two integers) inside the point class - constructor/initializer.
    # helps to save the data in the dictionary(instance dictionary).
    def __init__(self, a, b):
        # instance data
        self.a = a
        self.b = b

    # creating instance methods to manipulate the saved data of the calling instance
    def reset(self):
        self.a = 0
        self.b = 0

    def move(self, dx, dy):
        self.a = self.a + dx       # self.a += dx
        self.b = self.b + dy       # self.b += dy

    def sort(self):
        if self.a > self.b:
            self.a, self.b = self.b, self.a
            return self.a, self.b
        return self.a, self.b

    def total(self):
        return self.a + self.b

# ************* creating instance of point class *********************
# passing positional arguments
p1 = Point(1, 2)    # Point.__init__(p1, 3, 4)
p2 = Point(3, 4)    # Point.__init__(p2, 3, 4)

# passing keyword arguments
p3 = Point(a=5, b=6)    # Point.__init__(p3, 5, 6)

"""
* calls __init__() internally --> instances will be pointing to a built in dictionary
* data will be stored in the data structure dictionary - all the methods will take this dictionary
as first argument by default(i.e self)
"""

# ************************** Accessing the values of the class *********************
# syntax - (object.variable)
print(p1.a)     # 1
print(p1.b)     # 2

# *************************** Accessing functions of the class *************************
p1.reset()  # resets the data present in only p1
            # Point.reset(p1) - python internally does this
p2.reset()  # Point.reset(p2)
p1.move(0.1, 0.3)       # Point.move(p1, 0.1, 0.3)

print(dir(p1))  # gives the list of operations that can be performed on p1

# *************************** accessing instance dictionary ********************************
""" __dict__ -> returns the instance dictionary """
# modification of the instance dictionary directly is possible but should not be done.

print(p1.__dict__)      # {"a": 1, "b": 2}
print(p2.__dict__)      # {"a":3, "b": 4}

"""
There will be 2 dictionaries in a class
1. Instance dictionary
    - stores instance data / information about the actual data
    - there can be many instance dictionaries i.e, each instance will have its
      own dictionary 
    
2. class dictionary
    - there can be only one class dictionary 
    - stores the details of the methods and class data present inside the   
      class
      {class_variable: value, method_name: address_of_the_method}
    
"""

