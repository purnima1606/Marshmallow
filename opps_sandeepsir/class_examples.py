# passing the values from the dictionary to the functions
# numbers = {"a": 1, "b": 2}
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b

# passing values separately
# add(numbers["a"], numbers["b"])     # add(1, 2)
# sub(numbers["a"], numbers["b"])
# mul(numbers["a"], numbers["b"])

##########################################################################
# passing a dictionary and accessing the value in the methods
# numbers = {"a": 1, "b": 2}
#
# def add(data):
#     return data["a"] + data["b"]
#
# def sub(data):
#     return data["a"] - data["b"]
#
# def mul(data):
#     return data["a"] * data["b"]

# passing the dictionary itself
# add(numbers)        # add({"a": 1, "b": 2})
# sub(numbers)
# mul(numbers)

##############################################################################
# Instead of us passing a dictionary manually build a class that can pass the
# data as dictionary by default

# class Calculator:
#
#     # without init(), the instance dictionary will be empty
#     # x, y - local variables and will not be stored in instance dictionary
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
# c = Calculator(1, 2)
# print(c.__dict__)       # {"a": 1, "b": 2}
# c.add()     # Calculator.add(c) - passing c dictionary to add method

############################################################################

# class Player:
#     def __init__(self, x, y):
#         print("calling __init__")
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def attack(self, pts):
#         self.health -= pts
#
# p1 = Player(0, 0)
# p2 = Player(1, 2)
# print(p1.__dict__)      # {'x': 0, 'y': 0, 'health': 100}
# print(p2.__dict__)      # {'x': 1, 'y': 2, 'health': 100}
# p1.attack(20)   # takes the data from dictionary pointed by p1 and modifies it
# p2.attack(50)   # takes the data from dictionary pointed by p2 and modifies it

##############################################################################
# class Employee:
#
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     def email(self):
#         return f"{self.fname}.{self.lname}@company.com"
#
#     def pay_hike(self, hike):
#         hike_per = hike / 100
#         self.pay += self.pay * hike_per
#         return self.pay
#
# e1 = Employee("Steve", "Jobs", 1000)
# print(e1.email())  # Employee.email(e1)
# print(e1.pay_hike(20))
#















