# #################################################################
#
# # class demo:
# #     pass
# #
# # obj = demo()
# # print(obj)     # <__main__.demo object at 0x000001E7988ED108>
# # print(type(obj))   # <class '__main__.demo'>
# # print(obj.__dict__)  # {}
#
# ###################################################################
#
# # class Calculator:
# #
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #
# #     def add(self):
# #         return self.a + self.b
# #
# #     def sub(self):
# #         return self.a - self.b
# #
# #     def mul(self):
# #         return self.a * self.b
# #
# #     def div(self):
# #         return self.a // self.b
# #
# #
# # c = Calculator(5, 2)         # Object
# #
# # print(c.add())   # 7
# # print(c.mul())   # 10
# #
# # print(c.div())   # 2
# # print(c.sub())   # 3
# #
# # print(c.__dict__)        # {'a': 5, 'b': 2}  ---> Instance Dictionary
#
# ###############################################################################################
#
# # class Player:
# #
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #         self.heath = 100
# #
# #     def attack(self, pts):
# #         self.heath -= pts
# #
# #
# # p1 = Player(1, 2)
# # p2 = Player(3, 5)
# #
# # print(p1.__dict__)    # {'a': 1, 'b': 2, 'heath': 100}
# # print(p2.__dict__)    # {'a': 3, 'b': 5, 'heath': 100}
# # print(p1.attack(10))  # None
# # print(p1.__dict__)    # {'a': 1, 'b': 2, 'heath': 90}
# # p2.attack(20)
# # print(p2.__dict__)    # {'a': 3, 'b': 5, 'heath': 80}
# #
#
# #################################################################################################################
#
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def reset(self, a, b):
#         self.a = 0
#         self.b = 0
#
#     def move(self, x, y):
#         self.a += x
#         self.b += y
#
#     def sort(self):
#         if self.a > self.b:
#             return self.b, self.a
#         return self.a, self.b
#
#     def total(self):
#         return self.a + self.b
#
#
# p = Point(3, 4)
# p1 = Point(1, 2)
# print(p.__dict__)        # {'a': 3, 'b': 4}
# print(p1.__dict__)       # {'a': 1, 'b': 2}
# p.move(2, 3)
# print(p.__dict__)        # {'a': 5, 'b': 7}
# print(p.sort())          # (5, 7)
# print(p.total())         # 12
# print(p)                 # <__main__.Point object at 0x000002EDF5882608>
# print(dir(p))
#

# ******************************************************************************************************
class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

    def pay_hike(self, hike):
        pay_hike = hike / 100
        self.pay += self.pay * pay_hike
        return self.pay


e1 = Employee("steve", "jobs", 1000)
print(e1.__dict__)             # {'fname': 'steve', 'lname': 'jobs', 'pay': 1000}
print(Employee.email(e1))      # steve.jobs@company.com
print(e1.email())              # steve.jobs@company.com




















