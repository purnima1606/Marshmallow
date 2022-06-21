# s = "sonyindia"
# # india ia
# x ="i"
# for index, char in enumerate(s):
#     if char == x:
#         print(s[index: :], end=" ")              #  india ia



""" Square of element by using function """

# def square_(element):
#     return element ** 2
#
# print(square_(4))      # 16


# l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# l = []
# def square_(list):
#
#     for i in list:
#         l.append(i ** 2)
#
#     return l
#
# print(square_(l1))             #  [4, 9, 16, 25, 36, 49, 64, 81, 100]

######  square of value which is present inside a dictionary ############

# d = {"a":1, "b":2, "c":3}
# d1 = {}
#
# def square_(d):
#
#     for key, value in d.items():
#         d1[key] = value ** 2
#
#     return d1
#
# print(square_(d))         #  {'a': 1, 'b': 4, 'c': 9}

####### square of value which is present inside set #####

# s = {5, 3, 7, 2, 9}
# s1 = set()
# def square_(s):
#
#     for i in s:
#         s1.add(i ** 2)
#     return s1
#
# print(square_(s))            # {4, 9, 81, 49, 25}

""" Note: if I want to output in the same data type that we have to pass """
# l = []
# def square_(collection):
#     for i in collection:
#         l.append(i ** 2)
#
#     if isinstance(collection, list):
#         return l
#     elif isinstance(collection, tuple):
#         return tuple(l)
#     elif isinstance(collection, set):
#         return set(l)
#
# print(square_([2, 3, 4, 5]))         # [4, 9, 16, 25]
# print(square_((2, 3, 4, 5)))         # (4, 9, 16, 25, 4, 9, 16, 25)
# print(square_({2, 3, 4, 5}))         # {16, 9, 4, 25}
#

""" sort the list"""
# l = [100, 10, 30, 99, 101, 500, 1000]
# print(sorted(l))         # [10, 30, 99, 100, 101, 500, 1000]

# x = l.sort()
# print(l)       # None

# l.sort()
# print(l)   # [10, 30, 99, 100, 101, 500, 1000]



# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
""" 1. given two int a & b in one step you can add 2 to any num a or b
# your have to """
#
# def add_value(a, b):
#     if a > b:
#         print(b, b+2)
#     else:
#         print(a, a+2)
#
# add_value(2, 8)

# ????????????????????????????????????????????
""" delete middle of each """
# # l = [1, 2, 3, 4, 5]
# l1 = [10, 20, 30, 40]
#
# res = []
#
# def delete_middle(list_):
#
#     if len(list_)%2 != 0:
#         index_of_middle = len(list_)//2
#         # print(index_of_middle)
#         for i in range(len(list_)):
#             if i == index_of_middle:
#                 pass
#             else:
#                 res.append(list_[i])
#     else:
#         index_of_middle = len(list_)//2                       # (len(list_)//2)-1  => [10, 30, 40]
#         for i in  range(len(list_)):
#             if i == index_of_middle:
#                 pass
#             else:
#                 res.append(list_[i])
#
# # delete_middle(l)
# # print(res)      # [1, 2, 4, 5]
#
# delete_middle(l1)
# print(res)    # [10, 20, 40]

""" solve this using class """


"""  s = "Python Welcome Jayashr world mediumn hi """

# s = "Python Welcome Jayashr world mediumn hi"

# d = {item:len(item) for item in s.split()}
# res = dict(sorted(d.items(),key = lambda item : item[-1]))
# print(res)     # {'hi': 2, 'world': 5, 'Python': 6, 'Welcome': 7, 'Jayashr': 7, 'mediumn': 7}
# last_item = res.popitem()
# print(last_item)    # ('mediumn', 7)


# l = [item for item in s.split()]
# res = sorted(l, key=len)
# print(res)    # ['hi', 'world', 'Python', 'Welcome', 'Jayashr', 'mediumn']
# print(res[-1])   # mediumn

""" WAP to print all the second largest word in the given list """

# l = ['hai', "hello", "Not", "a", "Google", "world", "yahooo"]
# l1 = [len(item) for item in l]
# print(l1) # [3, 5, 3, 1, 6, 5, 6]
#
# res = list(set(l1))
# print(res)  # [1, 3, 5, 6]
#
# max_ = res[-2]
#
# for i in l:
#     if len(i) == max_:
#         print(i ,len(i),end="")
#         break


""" waf to return 3 digit numbers only """

# def return_3digit(s):
#     s1 = str(s)
#     if len(s1) == 3:
#         print(s)
#
#     else:
#         print(s1[-3::])
#
#
# return_3digit(1234)    # 234
#
# return_3digit(123)     # 123

# ****
# l = [1, 2, 3, 4, 5]
# # n = 2
# n = 1
# for i in range(n):
#     res = l.pop()
#     l.insert(0, res)
#
# # print(l)    # [4, 5, 1, 2, 3]
# print(l)      # [5, 1, 2, 3, 4]



# def func(num, k):
#     s = str(num)
#     for i in s:
#         for i in range(4):
#             if i[0]:
#                 p = int(i)+1
#                 for i in range(6):
#                     if i[1]:
#                         q = int(i)+1
#     return (p)
# print(func(512,10))

# ??????????????????????????????????????????????????????????????????????


""" If u get a new project are u able to create basic setups w. r. t to selenium configuration files"""


"1. Create a function should accept one argument as a string and u have to fetch the data from a file and u have map "
"the words and get the count of it they asked "


" 2. Function should accept a list and and if any number divisible by 3 then modify to 33 or else keep it as it is"

# l = [1, 2, 3, 4, 5, 6, 8, 9]
# res = []
#
# def div_(list_):
#
#     for i in list_:
#         if i % 3 == 0:
#             res.append(33)
#         else:
#             res.append(i)
#
# div_(l)
# print(res)   # [1, 2, 33, 4, 5, 33, 8, 33]



""" What are Abstract method and abstract class, base class.. How it work

If new class is created how is it possible access the abstract class .. Clarify the answer """


""" write a program to read excel"""

""" how will u Handle partial dynamic element """

""" palindrome without for loop """

"""  WAGF to generate first n value    """

#
# def gener_first_value(n):
#
#     i = 1                   # using while loop
#     while i <= n:
#         yield i
#         i += 1
#
#     # for i in range(1,n+1):          # using for loop
#     #     yield i
#
#
# g = gener_first_value(5)
#
# for value in g:
#     print(value, end=" ")

""" WAGF  to generate sequence of reverse order """
#
# def reverse_order(n):
#
#     for i in range(n, 0,-1):
#         yield i
#
# g = reverse_order(5)
#
# for i in g:
#     print(i, end=" ")

""" """

# def square_list(l):
#
#     for i in l:
#         yield i ** 2
#
#
# g = square_list([1, 2, 3, 4, 5])
#
# print(list(g))    # [1, 4, 9, 16, 25]
# # for i in g:
# #     print(i)

""" """
import time

def p_outer(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(n)
            func(*args, **kwargs)
            end = time.time()
            print(f"execution time of function is {end - start}")
        return wrapper
    return delay


@p_outer(2)
def multiplication_(a, b):

    print(a * b)


multiplication_(3, 4)

















