# all keyword are python in lower case :
# assigned one value to another data
# a = 2
# print(a)
# a= [1, 4, 5, 6, 7]
# print(a)

# maximum value of integer    ................>
# no limit ..... False

# one object two reference
# a =100
# b = a

# output of the following expression
# isinstance((1+2j) , (int, float, bool))
#  False

""" 2 ."""
# language = ["python", "c++", "java", "perl", "ruby"]
# res = language[2:4]
# print(type(res), res)     # list  , ["java", "perl"]

# string = "python"
# res = " ".join(string)
# print(res)

# get hai
# s = "%%%&^@#hai*&^^^%hello&&&&%"
# res = s.strip("%^*&@#ello")
# print(res)
""" we can not extract"""

#
# string = "fast and furious 3"
# print(string.isalnum())                # false **************


# string = "jack a\nd jill we\nt up \to hill"
# print(string)        # jack a
                     # d jill we
                     # t up 	o hill


# names = ["harry potter", "dumbledore", "voldemort"]
# names.extend(["ron"])
# print(names)           # ["harry potter", "dumbledore", "voldemort", "ron"]
# names.extend("ron")
# print(names)      # ["harry potter", "dumbledore", "voldemort","r","o","n"]

# string = "mary had a little lamb"
# print(string[:-3])     # mary had a little l

# languages = ["python", "c++", "java", "perl", "ruby"]
# languages.pop(-3)                # java           # pop(pos) in list
# # if use print statement then print java else nothing

# list1 = [1, 2, 3]
# list2 = list1.copy()
# print(list1 == list2)           # True

# avengers = ["iron man", "thanos", "captain america", "thor", "hawk eye", "groot"]
# # print(avengers.pop(1))
# print(avengers.remove("thanos"))
# print(avengers)


# data = ["python",[82,2+3j,["ruby","perl"]],"java"]
# print(data[1][1][2])           # type error

# output of the below code
# word = "corona"
# print(word.split())    # ['corona']

# string ="twinkle twinkle little star"
# print(string[-2:-5])   # nothing ,empty
#  -2 to -5 reverse but not mention step size = -1

# s = bool("hello".find("z"))
# print(s)    # True... bool(-1) = True

# l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None]
# print(l.sort())           # error .. diffrent data  type so we will get error,sort apply on same data type:

# l = ["Marry", "had", "a", "little", "lamb"]
# print(l.sort())                 # None
# print(l)                        # ['Marry', 'a', 'had', 'lamb', 'little']
# print(sorted(l))                # ['Marry', 'a', 'had', 'lamb', 'little']


# string = "today is friday"
# p = string[::]
# print(p)               # today is friday   .... not using [::-1]

# string = "today is friday"
# # print(string.split(2))      # Type Error
# print(string.split("2"))    # ['today is friday']

# sentence = "everyone must have felt bad when lron man died in the last season"
# print(sentence.find("thor"))

# str1 = "python"
# str1[1] ="x"     # not change the value of string once created
# print(str1[0:9])
# print(str1[2])

# sentence = "how much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(sentence.rindex("chuck"))       # 59

""" 3 """
# a = {1, 2, 3, 4}
# a.add({1, 2, 3, 4})       # not add sub set inside set
# print(a)

# d1 = {"one": 1, "two": 2, "three": 3}
# print(dict.fromkeys(d1))        # {'one': None, 'two': None, 'three': None}

"""d1 = {"one": 1, "two": 2, "three": 3, "four": 4}
d2 = {"three": 3, "five": 5, "two": 2}
print(**d1, **d2)
"""

# nums = {"ONE": 1, "TWO": 2}
# print(nums["one"])   # type error


# item() will return :
# list of tuples

# a = {"apple", "orange", "kiwi"}
# a.remove("mango")         # error

# output of the following:
# country_code = {"indra": 8464, "australia": 9645, "nepal": 9474}
# country_code.setdefault("japan", "not present")
# print(country_code)   # {'indra': 8464, 'australia': 9645, 'nepal': 9474, 'japan': 'not present'}


# a = {1, 2, 3, 4}
# b = {4, 3, 6, 7}
# a.symmetric_difference(b)
# print(a)          # {1, 2, 3, 4}


# a = {1, 2, 3, 4, 5, 6, 7}
# b = {3, 4, 6}
# print(b.issuperset(a))          # False

# output of the following code
# a = {1: ["apple", "amazon"], 2: ["flipkart"], 3: ["myntra"]}
# a["1"] = ["walmart"]
# print(a)       # {1: ['apple', 'amazon'], 2: ['flipkart'], 3: ['myntra'], '1': ['walmart']}


# li =[10, 1, 9, 8, 2, 7, 3, 6, 4, 5]
# print(sum(li))    # 55

# strip() removes the leading and trailing character of the original string
# False

# a = {1, 2, 3, 4}
# print(a.pop(0))    # type error


# to delete a key value pair in a dictionary use.............
# d = {"1": 45, "2": 30}
# print(d.remove("1"))        # remove not work here
# d.del()               # not work here
# d.pop("1")               # correct
# print(d)

# a = {1, 2, 3, 4}
# b = {4, 3, 6, 7}
# a.difference_update(b)
# print(a)             # {1, 2}


# give a index of brazil
# countries =("india", "bangladesh", "myanmar", "brazil", "britain")
# print(countries.index("brazil"))      # 3
# print(countries.find("brazil"))

"""
Built-in-fucntion of string:
1. index()
2. find()
Both are using to identifying the index of the required substring but the only difference between index & find is:
if the substring is not present inside the string then 
    index   =>  Error
    find    =>  -1

"""

# set allow all the data types as it's member:...
# no False


# print({1, 2, 3} + {3, 4, 5})                # error not posible in set

# output of the following :
# names = ("bob the ulu", "thomas", "sponge bob", "tom", "jerry mad")
# print(names[::2])      # ('bob the ulu', 'sponge bob', 'jerry mad')


# d1 = {"one": 1,"two": 2, "three": 3, "four": 4}
# d1.update({"six": 6})
# print(d1.popitem())       # ('six', 6)

# what is the output of the following code
# a = (1,)
# b = (1, 2, 3)
# # print(a + b)   # (1, 1, 2, 3)
# a = (*a, *b)
# print(a)    # (1, 1, 2, 3)

# d = {1: ["apple", "amazon"], 2: ["flipkart"], 3: ["myntra"]}
# print(d["1"])         # key Error

# dictionary is an unordered collection of key-value pairs             # correct ***************

# represent an empty set                               # set()

# output expression
# l = [10, 1, 9, 2, 8, 3, 7, 6, 4, 5]
# print(max(l))                  # 10

# split() separates each elements of string and returns the output in list format ************** # True

# output of the following :
# a = {1, 3, 5, 7}
# b = {2, 4, 6}
# print(b.isdisjoint(a))     # True

# output of the following
# a = {1, 2, 3, 4}
# b = {4, 3, 6, 7}
# a.union(b)
# print(a)    # {1, 2, 3, 4}

# output of the following
# l = [10, 90, 8, 7, 6, 5, 4, 3, 2, 1, None]
# l.sort()
# print(l)                    # error

# the memory location of string and s is the same in following code:
# string = "today is friday"
# s = string[::]    # True

# what is the return type of the 0/1 following ?
# names = ("bob the builder", "thomas", "sponge bob", "tom", "jerry")
# print(type(names[2]))                # <class str>

# output of the following?
# l = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# print(min(l))              # 1

# output of the following code:
# d1 = {"one": 1, "two": 2, "three": 3, "four": 4}
# d2 = {"two": 4, "three": 5, "five": 5}                    # **************************
# print(d1 + d2)   # type error

# output of the following :
# a = ["python", [22, 30], "java"]
# a[1][0] = 222
# print(a)            # ['python', [222, 30], 'java']

""" 7. function """
# specifying/ in the function definition means :
#                                                                ***********************************

# output

#
# def func(a:int, b:int):
#     return a,b
#
#
# print(func("hai", "hello"))     # ('hai', 'hello')

# output


# def spam():
#     return 1
#     return 2
#
#
# print(spam())        # 1


# return type of*args and **kwargs ? ** tuple and dictionary


# def spam(**kwargs):
#     print(kwargs)
#
#
# spam(a=1, b=2, c=3)      # {'a': 1, 'b': 2, 'c': 3}

# output
# def spam():
#     pass
#
#
# print(spam())           # None

# output
# def display(*args):
#     print(args)
#
#
# display(a=1, b=2)        # type error

# output
# def func(a,b,*,/,c,d):
#     print(a,b,c,d)
#
# func(1, 2, c=3, d=4)      # syntax error

# a function can be called before the function definition       # no False

# def function(*, a, b):
#     print(a, b)
#
#
# function(1, 2)                # error


# def spam(**kwargs):
#     print(kwargs)
#
#
# spam(a = 1, b = 2)        # error a=1

# def spam(*a):
#     print(a)              # (1, 2, 3)
#
#
# spam(1, 2, 3)

#def function():
#     return 1, "hai", [1, 2, 3]
#
#
# print(function())         # (1, 'hai', [1, 2, 3])

# def display(name = "steve"):
#     print(name)
#
#
# display(None)       # None

# def display(1, 2):           # parameter can not be integer
#     return
#
#
# display()                    # error

# specifying * in the function definition means # ***********************************************

# def spam(*args):
#     print(type(args))  # <class 'tuple'>
#
#
# spam(1, 2, 3)

# def func(a:int,  b:str) :
#     print(a, b)       # hai hello
#
#
# func("hai","hello")

# def spam(**kwargs, *args):
#     print(kwargs,args)     # syntax error
#
# spam(a=1, b=2, 3, 4)

# def spam():    # --> int
#     return "hai"
#
#
# print(spam())

"""    recursion       """
# a = 10
#
#
# def fun1():
#     global a
#     a += 20
#
# print(a)         # 10
# fun1()

# import sys
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())             # 10000

# output


# def recursive_func(string):
#     print(string)
#     return recursive_func(string[1::])
#
#
# recursive_func("hai")                # nothing

# output

# a = 10
# def fun1():
#     a = 20
#
#
# print(a)
# func()

# output
# a, *, b = [1, 2, 3, 4]
# print(a, *, b)                      # syntax error

#output
# a,_,b = [1, 2, 3, 4]
# print(a,_,b)                 # value error


# maximum recursion limit in python = 1000

# give a alias name with the help of ..........  as keyword

# in order to use a local variable inside a nested function, we need to make use to keyword called ...... nonlocal

# a function can pack both positional as well as keyword arguments .......... True

# output
# import sys
# print(sys.setrecursionlimit(10000))      3 none ************************

# output
# a = 10
#
# def fun1():
#     a += 20
#
#
# fun1()
# print(a)         # UnboundLocalError: local variable 'a' referenced before assignment

# a recursive function can be written without a base condition.       # False

#a = 10
# def fun1():
#     a = 20
#     def fun2():
#         a += 2           # syntax error
#         print(a)         # UnboundLocalError: local variable 'a' referenced before assignment
#     fun2()
#
# fun1()

# a variable present outside the function is called ..... global variables

# which of the following method returns the maximum recursion depth ?..........# sys.getrecursionlimit()

# a, *z, b = (1, 2, 3, 4)
# print(a, b, z)       # 1 4 [2, 3]

# we can open multiple file in a single block... False

# csv.writer() will create an object which takes the arguments only in the form of  **************

# the return datatype of readlines() is   **********************

# when a file is created in create mode, it will throw error if, **********************

# we can open multiple files with different modes at a time **************

# csv.DictWriter() accepts the following arguments

# by default a file will be opened in .... read mode

# if i want to create a list comprehension for reading a file then i'll use the following syntax ***************






















l = (1, "hai", (1, 2, 3), "vidya", 2+4j, 3.7)
