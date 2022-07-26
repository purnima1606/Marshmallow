                                  # Basic Programs:

""" Python program to add two numbers"""

# a = 10
# b = 20
# a = int(input("enter the value of a"))
# b = int(input("enter the value of b"))
# print(a+b)

""" Maximum of two numbers in Python  """

# a = int(input("enter the value of a:"))
# b = int(input("enter the value of b:"))
# if a > b:
#     print(a)
# else:
#     print(b)

""" Python Program for factorial of a number """

# n = int(input("enter the factorial number:"))
# a = 0
# b = 1
# c = 0
# for _ in range(n+1):
#     print(c)
#     a = b
#     b = c
#     c = a + b

""" Python Program for simple interest """
# p = initial principle balance
# r = annual interest rate
# t = time(in year)
#
# p = int(input("enter the initial principle balance:"))
# r = int(input("enter the annual interest rate:"))
# t = int(input("enter the time (in year):"))
#
# si = p * r * t
# print(si)

""" Python Program for compound interest """
# p = initial principle balance
# n = number of times interest applied per time period
# r = interest rate

# p = int(input("enter the initial principle balance:"))
# r = int(input("enter the annual interest rate:"))
# n = int(input("enter the numbers of times"))
#
# ci = p * ((1 + (r/100) )** n) - p
# print(ci)

""" Python Program to check Armstrong Number """

# s = int(input("enter the number:"))
# res = ""
# for i in str(s):
#     res = i + res
#
# if str(s) == res:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")


""" Python Program for Program to find area of a circle """
# a = (22/7)r ** 2

# r = int(input("enter the radios of the circle:"))
# a = (22/7) * r ** 2
# print(a)



""" Python program to print all Prime numbers in an Interval """

# n = int(input("enter a number"))
# count = 0
#
# for i in range(n+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


"""Python program to check whether a number is Prime or not"""
# n = int(input("enter the number:"))
# for i in range(2,n):
#     if n % i == 0:
#         print(f"{n} is not a prime number:")
#         break
# else:
#     print(f"{n} is a prime number:")


"""Python Program for n-th Fibonacci number"""
# n = int(input("enter the number:"))
# count,a, b, c = 0,0,1,0
# for _ in range(n+1):
#     count += 1
#     if n == count:
#         print(f"{n} fibonacci number is {c}")
#     else:
#         # print(c)
#         a = b
#         b = c
#         c = a + b

"""Python Program for How to check if a given number is Fibonacci number?"""

# n = int(input("enter the number:"))
# a,b,c = 0,1,0
# for i in range(n+1):
#     if c == n:
#         print("given number is Fibonacci number")
#     else:
#         a = b
#         b = c
#         c = a + b
# else:
#     print("given number is not Fibonacci number")


""" Python Program for n\’th multiple of a number in Fibonacci Series"""




"""Program to print ASCII Value of a character"""
# c =input("enter any one character:")
#
# print(ord(c), c)

"""Python Program for Sum of squares of first n natural numbers"""

# n = int(input("enter the number"))
# for i in range(n+1):
#     sum += i ** 2
# print(sum)

"""Python Program for cube sum of first n natural numbers"""
# n = int(input("enter the number"))
# for i in range(n+1):
#     sum += i ** 3
#
# print(sum)
