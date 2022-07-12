






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

"""" Function,one program ,that to reverse the string """
# method 1
# def reverse_(s):
#     print(s[::-1])
#
# reverse_("python")

# method 2

# def rev(s):
#     res = ""
#     for char in s:
#         res = char + res
#     return res
#
# print(rev("python"))

""" program to print only even numbers from a list """

# def even(l):
#     for item in l:
#         if item % 2 == 0:
#             print(item, end=" ")
#
#
# even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

""" o/p = [10,7,4,1] """
a = [1,2,3,4,5,6,7,8,9,10]

# print(a[::-3])

""" 
a,b,c,d = 1,2,3,4,5
a=1,b=2,c=[3,4],d=5
a = ? ,b = ?, c= ?, d= ?
"""
#
# a, b, *c, d =1, 2, 3, 4, 5
# print(a, b, c, d)

""" 10.Explain slicing """


""" Take one string(using slicing method) he told to extract some characters in string """
s1 = "python is simple language"

# print(s1[:6])
# print(s1[7:9])
# print(s1[10:16])
# print(s1[17:])
#
# print(s1[:9])
# print(s1[:16])
#
# print(s1[1:6])
# print(s1[2:9])
# print(s1[7:13])
# print(s1[13:16])


# print(s1[-1:-9:-1])
# print(s1[-10:-16:-1])
#

""" WAP to create random nummer """
# import random
#
# print(random.randint(1, 101))

# import time
#
# current_time = time.localtime(time.time())
# print(current_time)

"""
1. self introduction 
2. Tell me about your frame work which you used in your project 
4. Difference between smoke and sanity testing 
6. Can you tell about Defect life cycle 

7. i have 50 test cases , you are doing Regression testing , SO you have only 2 days of time to complete the 
  regression testing . the scenario is , you has to complete the regression testing with in end of day(today).
  Tomorrow is the release and you only the QA in your team , and you have 50 test cases . So how you can complete
  regression testing with in the day 
  
8. difference between list and dict 
9. difference between .py and .pyc



11. what are the keywords available in Python ?
import, True, False, is, in, not, if, else, elif, def, for, while, lambda, global, nonlocal, break, continue, pass, 
None, class, return, yield, try, except, finally, and, or, 

12.How to combine data frames ?

15.Explain OPP 
16.what is polymerphism ?

17.What is data Abstraction ? 
18.What is data Encapsulation ?
19.Explain Inheritance 

24.how you can going to sink the code from local repository to global repository ?
25.How can you revert the codes ?


27.what is sql ?
28.Find the 2nd highest sal and details of the employee from employee dynamic table 


"""

"""
keyword :-
if , else, elif, import ,True, False, None, break, continue, pass, def, class, return, yield, and, or, in, is, not, 

"""
# import keyword
#
# # print(help(keyword))
# print(keyword.kwlist)
#
# print(keyword.iskeyword("if"))


"""
13.6 reversed the item i.e o/p should be Singh Saurabh

s = "Saurabh Singh"

# 13.4 remove the duplicate items
print(set(s))
res = ""
for char in s:
    if char not in res:
        res += char

print(res)
# 13.5 remove the spaces in between

res = s.replace(" ", "")
print(res)

# 13.6 reversed the item i.e o/p should be Singh Saurabh
print(s[::-1])

for char in reversed(s):
    print(char, end="")
"""








