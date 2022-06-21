






""" 3) Explain Framework And oops concept """


""" 4) Where did you use Abstract class in your Project """


""" remove spaces in between the sentence """
# s = "Python is Programming Language"
#
# # method 1
# # res = s.replace(" ", "", 2)
# res = s.replace(" ", "")
# print(res)

# # method 2
# res = ""
# for char in s:
#     if char == " ":
#         continue
#     else:
#         res += char
#
# print(res)

""" count the no of characters in a string without using len """

# s = "Python is Programming Language"
# count = 0
#
# for char in s:
#     count += 1
#
# print(count)
# print(len(s))

""" find prime no to given range (100, 200)"""

# for num in range(100, 201):
#
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num ,end="  ")


""" find given no is prime or not """
#
# n = int(input("enter any number"))
#
# for i in range(2, n):
#     if n % i == 0:
#         print(f"{ n } is not prime")
#         break
# else:
#     print(f"{ n } is prime")

""" Decorators,one program """

# method 1

# def decor_sub(func):
#     def wrapper(*args, **kwargs):
#         res = abs(func(*args, **kwargs))
#         return res
#     return wrapper
#
#
# @decor_sub
# def sub(a, b):
#     return a - b
#
#
# print(sub(2, 3))

# method 2

#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, int):
#             return abs(res)
#         return f"********* {res} **************"
#     return wrapper
#
#
# @decor
# def sub(a, b):
#     return a - b
#
#
# @decor
# def add(a, b, c):
#     return a + b + c
#
#
# @decor
# def mul(a, b, c):
#     return a * b * c
#
#
# @decor
# def demo():
#     return " hello hii"
#
#
# print(sub(2, 6))
# print(add(3, 4, 6))
# print(mul(1, 2, 3))
# print(demo())


"""example 2: WADF that calculates time of execution of a function """
# import time
#
# # def outer(n):
# def decor(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print(start)
#         time.sleep(2)
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"execution time is {end - start}")
#     return wrapper
#     # return decor
#
#
# # @outer(2)
# @decor
# def add(a, b):
#     return a + b
#
#
# add(3, 5)

"""example 3: WADF to print "hello world" message if the user has not given input """
# method 1
# def decor(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if bool(res) == 0:
#             print("hello world")
#     return wrapper
#
#
#
# @decor
# def demo():
#     print("this is demo")
#
# demo()

# method 2

# def outer(string_):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             # print(res)
#             if bool(res) != True:
#                 print(string_)
#             else:
#                 print(res)
#         return wrapper
#     return decor
#
# @outer("hello world")
# def demo(msz=""):
#     return msz
#
# # demo()
# demo("welcome")


""" Apply multiple decorator on a single function """


# def decor1(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f"******** {res} ***********"
#     return wrapper
#
#
# def decor2(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f"$$$$$$$$$$$$$ {res} $$$$$$$$$$$$"
#     return wrapper
#
#
# @decor1
# @decor2
# def add(a, b):
#     return a + b
#
#
# print(add(3, 5))     # ******** $$$$$$$$$$$$$ 8 $$$$$$$$$$$$ ***********









