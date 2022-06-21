

""" decorator is a function which is takes a function as an argument and add some functionality without modifying original function
"""
# 1.
# def sub_decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
#
# @sub_decor
# def sub(a,b):
#     return a-b
#
# print(sub(2,5))


""" generator is a function which is generate sequence of value, generator is not consume space in memory
"""

# def sequence_value(sp, ep):
#     for i in range(sp,ep+1):
#         yield i
#
#
# g = sequence_value(0,10)
#
# for i in g:
#     print(i, end=" ")   # 0 1 2 3 4 5 6 7 8 9 10

""" comprehension is an elegant way to create /define new iterable
there are three type of comprehension:-
1. list comprehension 
2. set comprehension
3. dictionary comprehension  

 1. list comprehension => list comprehension is an elegant way to create /define  and modify new list
"""
# items = [item for item in range(1,11)]
# print(items)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# l = [item**3 for item in items]
# print(l)        # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

""" 2. set comprehension => set comprehension is an elegant way to create/define and modify new set 
"""
# s1 = {item for item in range(1,11)}
# print(s1)    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#
# s2 = {item**2 for item in s1}
# print(s2)                     # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

""" 3. dictionary comprehension => dictionary comprehension is an elegant way to create/define and modify new dictionary
"""
# s = "python is programming language"
# l = s.split()

# d1 = {word[0]:word for word in l}
# print(d1)     # we go for data loss

# d1 = {word:word[0] for word in l}
# print(d1)  # {'python': 'p', 'is': 'i', 'programming': 'p', 'language': 'l'}

# d1 = {word:len(word) for word in l}
# print(d1)       # {'python': 6, 'is': 2, 'programming': 11, 'language': 8}


""" NOTE: tuple comprehension is not posible because if we create tuple comprehension it will convert into generater fuction/expresion
"""

# **************************************************************************************************
"""  *********** INHERITANCE ************"""
""" inheritance is a process or phenomena inherit the propertice of one class(parant class) to another class(child class)
1. single level inheritance
2. multi level inheritance 
3. multiple inheritance
4. hararchal interitance
5. hybrid inheritance
"""
# 1. single level inharitance
# class Parant:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
# class child1(Parant):
#
#     def __init__(self,a,b):
#         super().__init__(a,b)
#
# p = Parant(4,2)
# print(p.add())    # 6
# print(p.sub())    # 2
#
# c = child1(5,3)
# print(c.add())    # 8
# print(c.sub())    # 2

""" 2. multi level inheritance """
# class Parant:
#
#     def demo(self):
#         print("parant demo: ")
#
#     def test(self):
#         print("parant test: ")
#
#
# class child1(Parant):
#
#     def demo1(self):
#         print("child1 demo1: ")
#
#
# class child2(child1):
#     pass
#
# c2 = child2()
# c2.demo1()
# c2.demo()
# c2.test()
#
# # child1 demo1:
# # parant demo:
# # parant test:

""" 3. multiple inheritance """
# class parant1:
#
#     def demo1(self):
#         print("parant1 demo: ")
#
#     def test1(self):
#         print("parant1 test: ")
#
#
# class parant2:
#
#     def demo2(self):
#         print("parant2 demo: ")
#
#     def test2(self):
#         print("parant2 test: ")
#
# class child(parant1, parant2):
#     pass
#
#
# c = child()
# c.demo1()
# c.demo2()
#
# c.test1()
# c.test2()
#
# # parant1 demo:
# # parant2 demo:
# # parant1 test:
# # parant2 test:

""" 4. Hierarchy inheritance """

# class parant:
#
#     def demo(self):
#         print("parant demo: ")
#
#     def test(self):
#         print("parant test: ")
#
#
# class child1(parant):
#     pass
#
# class child2(parant):
#     pass
#
#
# c1 = child1()
# c2= child2()
#
# c1.demo()
# c2.demo()
#
# c1.test()
# c2.test()
#
# # parant demo:
# # parant demo:
# # parant test:
# # parant test:

"""5. Hybrid inheritance """

# class parant:
#
#     def demo(self):
#         print("parant demo: ")
#
#     def test(self):
#         print("parant test: ")
#
#
# class child1(parant):
#     pass
#
#
# class child2(parant):
#
#     def example(self):
#         print("child2 example: ")
#
#
# class child3(child2):
#     pass
#
#
#
# c1 = child1()
# c2 = child2()
# c3 = child3()
#
# c1.demo()
# c1.test()
#
# c2.demo()
# c2.test()
# c2.example()
#
# c3.demo()
# c3.test()
# c3.example()

# parant demo:
# parant test:
#
# parant demo:
# parant test:
# child2 example:
#
# parant demo:
# parant test:
# child2 example:


""" polymorphism => it stands for many form /it means many form. 
there are two type 
1. overloading
    1.1 method overloading
    1.2 operator overloading
    1.3 constructor overloading
    
2. overridding
    2.1 method overridding
    2.2 constructor overridding
"""
# class parant:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     # def __init__(self,a, b, c):             # constructor overloading
#     #     self.a = a
#     #     self.b = b
#     #     self.c = c
#
#     def add(self):
#         print(self.a + self.b)
#
#     def add(self):                          # method overloading
#         print(self.a + self.b + self.c)     # operator overloading
#
#
#     def multiplication(self):
#         print(self.a * self.b)
#
# # p = parant(2,3,4)
# # p.add()    # 9
# # p1 = parant("hai","hai", "hai")
# # p1.add()             # haihaihai       => operator overloading
#
# p2 = parant("hello", 2)
# p2.multiplication()     # hellohello
#


"""   overridding """
# class perant:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# class child(perant):
#
#     def add(self):           # method overridding
#         print(self.a - self.b )
#
#
# c = child(5,3)
# c.add()       # 2


# class perant:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# class child(perant):
#
#     def __init__(self,a ,b ,c):      # constructor overridding
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def add(self):                   # method overridding
#         print(self.a + self.b +self.c)
#
#
# c = child(5,3,5)
# c.add()  # 13

""" encapsulation 
        data hidding
"""
#
# class perant:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b =b
#
#     def _add(self):
#         print(self.a + self.b)
#
#     def __sub(self):
#         print(self.a - self.b)
#
# class child(perant):
#     pass
#
# c = child(4,6)
# c._add()   # 10
# # c.__sub()        # AttributeError: 'child' object has no attribute '__sub'
#
# p = perant(4,3)
# p._sub()           # AttributeError: 'perant' object has no attribute '_sub'
#
# # by default everything is public in python


""" Abstaction
    data implementation hiding
    * Abstract Class
    * Abstract Method
"""
# from abc import ABC
#
#
# class Abstract(ABC):          # Abstract class
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def add(self):             # Abstract method
#         pass
#
#     def sub(self):
#         print(self.a - self.b)
#
#
# class child(Abstract):
#
#     def add(self):                      # implementation on Abstract method
#         print(self.a + self.b)
#
#
# p = Abstract(5,3)
# # p.add()
# p.sub()
#
# c = child(5,2)
# c.sub()
# p.sub()
#
# ??????????????????????????????????????????????????????????????

"""   Types of variable  """
"""   Type of method  """

# class demo:
#     a = 10                  # global variable
#     d = 20
#
#     def __init__(self,b ,c):
#         self.b = b            # instance variable
#         self.c = c
#
#     def add(self):
#         print(self.b + self.c)
#
#     @classmethod
#     def sub(cls):
#         print(cls.a - cls.d)
#
#     @staticmethod
#     def mul():
#         a = 3            # local variable
#         b = 5
#         print(a * b)
#
#
#
# d = demo(2,1)
# d.add()
# d.sub()
# d.mul()

""" class => class is a idea/blue print of object.
    object => object is a physical existances of class
    constructor => constructor is a special method which is responsible for create instance variable
                    when we create a object of a class ,constructor call automatically
                    name of constructor is __init__
    
    self => self is a variable, we can create or access instance variable inside the class.
                    
"""


""" data type """

# 1. string
# s = "hello"
# s1 = "hii"
#
# print(s+s1)          # hellohii


# 2. list
# l = [1, 2, 3]
# l1 = [4, 5, 6]
#
# print(l+l1)            # [1, 2, 3, 4, 5, 6]
# print(*l, *l1)         # (1 2 3 4 5 6)
# print([*l, *l1])       #  [1, 2, 3, 4, 5, 6]

# 3. tuple
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
#
# print(t1+t2)              # (1, 2, 3, 4, 5, 6)
# print(*t1, *t2)           # (1 2 3 4 5 6)
# print((*t1,*t2))          # (1, 2, 3, 4, 5, 6)

# 4. set

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
#
# print(*s1, *s2)  # 1 2 3 4 5 6


# 5. dictionary

# d1 = {"a":1, "b":2, "c":3}
# d2 = {"d":4, "e":5, "f":6}
#
# # print(**d1,**d2)     # Error
# print({**d1,**d2})     # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}









