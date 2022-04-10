# class calculator:
#     def _init__(self, x, y):
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
#
# c = calculator(2, 4)
# # print(c.add())
# print(c.__dict__)

#############################################################################################
# class player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.heath = 100
#
#     def attack(self, pts):
#         self.heath -= pts
#
#
# p1 = player(0, 0)
# p2 = player(1, 2)
# print(p1.__dict__)      # {'x': 0, 'y': 0, 'heath': 100}
# print(p2.__dict__)      # {'x': 1, 'y': 2, 'heath': 100}
# p1.attack(20)
# print(p1.heath)
# print(p1.__dict__)

###############################################################################################

# class point:
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#
#     def reset(self):
#         self.a = 0
#         self.b = 0
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.b += dy
#
#     def sort(self):
#         if self.a < self.b:
#             return (self.b, self.a)
#         return (self.a, self.b)
#         # if self.b < self.a:
#             # temp = self.a
#             # self.a = self.b
#             # self.b = temp
#
#         return (self.a, self.b)
#
#     def total(self):
#         return (self.a + self.b)
#

# p1 = point(1, 2)
# p2 = point(3, 4)
# print(p1.__dict__)              # {'a': 1, 'b': 2}
# print(p2.__dict__)              # {'a': 3, 'b': 4}
# print(p1.a, p1.b, p2.a, p2.b)   # 1 2 3 4
# print(p1.sort())                # (1, 2)
# print(p2.sort())                # (3, 4)
# print(p1.move())

#########################################################################################3
