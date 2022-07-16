""" ** 1. Write a program to find the length of the string without using inbuilt function (len) **"""
# s = "python is programing"
# count_ = 0
# for i in s:
#     count_ += 1
# print(count_)

# string_ = "hello how are you"
# count = 0
# for char in string_:
#     count += 1
# print(count)                   # 17
# print(len(string_))            # 17

""" **2. Write a program to reverse a string without using any inbuilt functions.**"""
# s = "lion is king"
# for i in reversed(s):
#     print(i , end="")  # gnik si noil

# s = "hello world hi how are you"
# res = ""
# for char in s:
#     res = char +res
# print(res)
# # r = reversed(s)
# # print(r)
#


"""**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**"""
# s = "Hello World"
# r = s.replace("World", "Universe")
# print(r)

# s = "Hello World"
# print(s.replace("Hello World", "universe"))      # universe

"""**4. How to convert a string to a list and vice-versa.**"""

# s = "python is easy language"
# res = []
# for i in s.split():
#     res.append(i)
#
# print(res)
# print(" ".join(res))

# s = "hi how are you"
# # string to list
# list_ = s.split()
# print(list_)
# # list to string
# s1 = " ".join(list_)
# print(s1)

"""**5. Convert the string "Hello welcome to Python" to a comma separated string.**"""
# s = "Hello welcome to Python"
# res = s.split()
# print(",".join(res)) # Hello,welcome,to,Python


# s = "Hello welcome to python"
# l = s.split()
# res = ",".join(l)
# print(res)            # Hello,welcome,to,python

"""**6. Write a program to print alternate characters in a string.**"""
# s = "Hello welcome to Python"
# print(s[::2])    # Hlowloet yhn

# s = "hi how are you"
# print(s[::2])   # h o r o

"""**7. Write a Program to print ascii values of the characters present in a string.**"""
# s = "hello how are u"
# for i in s:
#     print(i, ord(i))


# s = "programming is fun"
# for char in s:
#     print(char, ord(char))


"""**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**"""
# s = "HoW aRe U"
# res = ""
# for i in s:
#     if i.islower():
#         res += i.upper()
#     elif i.isupper():
#         res += i.lower()
#     else:
#         res += i
#
# print(res)


# def upper_lower(n):
#     res = ""
#     for char in n:
#         if "a" <= char <= "z":
#             res += chr(ord(char)-32)
#         elif "A" <= char <= "Z":
#             res += chr(ord(char)+32)
#         else:
#             res += char
#     return res
#
#
# print(upper_lower("HeLLo 123WorLD"))    # hEllO 123wORld

"""**9. Write a program to swap two numbers without using the 3rd variable.**"""
# a , b = 10, 20
# print(a, b)
# a, b = b, a
# print(a, b)

# a, b = 10, 20
# print(a, b)
# a, b = 20, 10
# print(a, b)

"""**10. Write a program to merge two different lists.**"""

# l1 = [1,2,3]
# l2 = [4,5,6]
# # print(l1+l2)  # [1, 2, 3, 4, 5, 6]
# # print([*l1,*l2])  # [1, 2, 3, 4, 5, 6]
# print(*l1,*l2)  # 1 2 3 4 5 6  i.e (1 2 3 4 5 6)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [*l1, *l2]
# print(l3)    # [1, 2, 3, 4, 5, 6]

"""**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**"""
# path = "file path"
# n = int (input("enter the line number:"))
# count_ = 0
# with open(path) as file:
#     for line in file:
#         count_ += 1
#         if count_ == n:
#             print(line)


# islice
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
# n = int(input("enter any random line number: "))
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if line.strip():
#             if count == n:
#                 print(line)       # n = 7  # 03/22 08:51:02 INFO   :..reg_process: attempt OS/390 registration

"""**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**"""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
# from itertools import islice
# with open(path) as file:
#     lines = islice(file, 4, 8)
#     for line in lines:
#         print(line)             # run
# ****************************************************
"""**13 Program to print the last "N" lines of a file.**"""
# from itertools import islice
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
# n = int(input("last n lines : "))
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     # print(count)      # 340
#     file.seek(0)
#     lines = islice(file, count-n, count)
#     for line in lines:
#         print(line)                 # run
# ****************************************************
"""**14. Write a program to check if the given string is Palindrome or not without using reversed method.**"""

# s = input("enter any string :")
# if s == s[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

"""**15 Write a program to search for a character in a given string and return the corresponding index."""
# s = "hello world"
# n = "w"
# for index, char in enumerate(s):
#     if char == n:
#         print(char, index)

"""**16 Write a program to get the below output"""

# sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcom0e'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# l = sentence.split()
# d = {}
# for char in l:
#     if char[0] not in d:
#         d[char[0]] = [char]
#     else:
#         d[char[0]] += [char]
#
# print(d)                    # {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}

"""**17 Write a to replace all the characters with - if the character occurs more than once in a string**"""
# my_string = 'hellohai' # O/P should be '-e--o-ai'           # ****************
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????/
"""**18 write a decorator that returns only positive values of subtraction**"""

# def decor(func):
#     def wrapper(*args, **kwargs):
#         return abs(func(*args, **kwargs))
#     return wrapper
#
# @decor
# def sub(a, b):
#     return a - b
#
#
# print(sub(2, 3))     # 1

"""**19 How to get the count of number of instances of a class that is being created.**"""   # *************
#?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

"""**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and 
if the item is integer of float it should reverse it.**"""
l = ["hello", 674, "hii", 983, "python"]  # **********
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# def reverse_digit(list_):
#     res = 0
#     for word in list_:
#         if isinstance(word, int):
#             x = word % 10
#             res = res + x
#             word = word // 10
#
#         else:
#             print(word)
#
#
# print(reverse_digit(l))

# reverse string :

# def reverse_digit(list_):
#     res = 0
#     for word in list_:
#         if isinstance(word, str):
#             print(word[::-1], end=" ")
#
#         else:
#             print(word, end=" ")
#
#
# reverse_digit(l)              # olleh 674 iih 983 nohtyp



"""**21 Write a class named Simple and it should have iteration capability.**"""
#?????????????????????????????????????????????????????????????????????
"""**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**"""
# __setitem__ or __setattr__
#>???????????????????????????????????????????????????????????????????????????????????????????????????
"""**23 Write a python program to get the below output**
     sentence = "Hi How are you"
     o/p should be "iH woH era uoy"
#???????????????????????????????????????????????????????????????????????????????????????????
**24 Write a python program to get the below output**
     sentence = "Hi How are you"
     o/p should be "ouy era woH iH"
"""
# ??????????????????????????????????????????????????????????????????????????????????????????????????????????
"""**25 Write a lambda function to add two numbers (a, b)**"""
# l = lambda a, b: a+b
# print(l(2, 3))       # 5

"""**26 What is the output of the following**"""
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])          # [[1, 2, 3], [4, 5, 6]]
# print((a, b))          # ([1, 2, 3], [4, 5, 6])

"""**27 How to remove duplicates from the list without using inbuilt functions**"""
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# def duplicate_(n):
#     l = []
#     for item in n:
#         if item not in l:
#             l.append(item)
#     return l
#
#
# print(duplicate_(items))        # [1, 2, 3, 4, 5]
# print(list(set(items)))         # [1, 2, 3, 4, 5]

"""**28 Find the longest word in the sentence**"""
# sentence = "python is programming language"           # ****
# l = sentence.split()
# l1 = lambda item: len(item)
# # res = map(sentence, key=len)
# # print(res)
# res = list(map(l, l1))
# print(res)
# min_, *r, max_ = res
# print(min_, max_)
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

"""**29 write a program to reverse the values in the dictionary if the value is of type String**"""

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
# print(d1)    # {'a': 'olleh', 'b': 100, 'c': 10.1, 'd': 'dlrow'}

"""**30 write a program to get 1234"""

# t = ('1', '2', '3', '4')
# res = "".join(t)
# print(int(res))    # 1234

"""**31 How to get the elements that are in list b but not in list a**"""
#     a = [1, 2, 3]
#     b = [1, 2, 3, 4]
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

"""**32 A function takes variable number of positional arguments as input. 
How to check if the arguments that are passed are more than 5**"""

# def check_arguments(*args):
#     count = 1
#     for i in args:
#         count +=1
#     return count
#
#
# print(check_arguments(1, 2, 3,4 ))             # 5

"""**33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# Assume Below is the contents of the log file
"""
lines = """
CRITICAL: Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error.
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error
CRITICAL: This is critical"""

# count = 0
# res = 0
# emp = 0
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\csv_files\sample.log2.py"
# with open(path) as file:
#     for lines in file:
#         line = lines.split()
#         for _ in line:
#             if line[0] in "INFO:":
#                 count += 1
#             if line[0] in "ERROR:":
#                 res += 1
#             if line[0] in "CRITICAL:":
#                 emp += 1
# print(count)
# print(res)
# print(emp)

# method 1
#d = {}
# list_ = lines.split("\n")
# for line in list_:
#     if line.strip():
#         words = line.split(":")
#         if words[0] not in d:
#             d[words[0]] = 1
#         else:
#             d[words[0]] += 1
#
#
# print(d)       # {'CRITICAL': 8, 'INFO': 4, 'ERROR': 4}


"""**34 Write a function to reverse any iterable without using reverse function."""
# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

"""**35 Write a function to print the below output.**"""
     # func("TRACXN", 0)  # Should print RCN
     # func("TRACXN", 1)  # Should print TAX

# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

"""**36 Sum all the numbers in the below string.**"""

# s = "Sony12India567Pvt2ltd"
# sum_ = 0
# for i in s:
#     if i.isdigit():
#         sum_ += int(i)
#
# print(sum_)   # 23


"""**37 Write a program to sum all the numbers in below string.**"""

# s = "Sony12India567Pvt2ltd" # eg.12+567+2
# import re
# sum = 0
# res = re.findall(r"\d+", s)
# print(res)         # ['12', '567', '2']
# for i in res:
#     sum += int(i)
# print(sum)       # 581

"""**38 Print all the numbers in the below list**"""

# a = ['abc', '123', 'hello', '23']
# sum_ = 0
# for i in a:
#     if i.isdigit():
#         sum_ += int(i)
# print(sum_)   # 146

"""**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**"""

# s = "hello world how are you"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# print(d)    # {'h': 2, 'e': 2, 'l': 3, 'o': 4, ' ': 4, 'w': 2, 'r': 2, 'd': 1, 'a': 1, 'y': 1, 'u': 1}

"""**40 Program to print only the repeated characters and count of the same.**"""

"""**41 Write a program to get alternate characters of a string in list format.**"""

# s = "hello world how are you"
# count = 0
# l = []
# for i in s:
#     count += 1
#     if i != " ":
#         if count % 2 != 0:
#             l.append(i)
#             # print(i, end=" ")   # h l o w r d h w a e y u
# print(l)      # ['h', 'l', 'o', 'w', 'r', 'd', 'h', 'w', 'a', 'e', 'y', 'u']

"""**42 Write a program to get square of list of number's using lambda function .**"""

# l1 = [1, 2, 3, 4, 5]
# l = lambda item: item**2
# res = list(map(l, l1))
# print(res)   # [1, 4, 9, 16, 25]

"""**43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**"""

# s1 = input("enter the string1:")
# s2 = input("enter the string2:")
#
# def anagram_(s1 ,s2):
#     if sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
#
#
# print(anagram_(s1, s2))
# enter the string1:tea
# enter the string2:ate
# True


"""**44 Write a program to iterate through list and build a new list, only if the items of the list has even number of characters.**"""

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# l = []
# for word in names:
#     if len(word) % 2 == 0:
#         l.append(word)
#
# print(l)  # ['google', 'flipkart', 'facebook', 'amazon']


"""**45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.**"""

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {}
# for word in names:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
#
# print(d)   # {'google': 6, 'flipkart': 8, 'facebook': 8, 'amazon': 6}

"""**46 Write a program which squares the numbers in a list using map object**"""

# a = [1, 2, 3, 4, 5]
# l = lambda item: item ** 2
# res = list(map(l, a))
# print(res)           # [1, 4, 9, 16, 25]

"""**47 Count number of lines in a file without loading the file to the memory**"""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(line)               # run

"""**48 Printing line and line no's**"""

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     for line, index in enumerate(file):
#         print(line, index)

"""**49 Write a Program to print the sum of entire list and sum of only internal list**"""

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum_ = 0
# for list_ in l:
#     inter_sum = 0
#     for digit in list_:
#         inter_sum += digit
#     print(inter_sum, end=" ")       # 6 15 24
#     sum_ += inter_sum
#
# print("\n")
# print(sum_)  # 45

"""**50 Write a program to reverse the list as below**"""

# words = ["hi", "hello", "python"]
# res = words[::-1]
# print(res)        # ['python', 'hello', 'hi']

"""**51 Write a program to update the tuple**"""

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
# # t3 = t1+t2        # (1, 2, 3, 4, 100, 200, 300)
# t3 = (*t1, *t2)
# print(t3)         # (1, 2, 3, 4, 100, 200, 300)

"""**52 Write a program to replace value present in nested dictionary.**"""
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"
# ????????????????????????????????????????????????????????????????
"""**53 Write a program to count the number of white spaces in a file.**"""

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += line.count(" ")
#
# print(count)            # 21

"""**54 Grouping anagrams.**"""
# ?????????????????????????????????????????????????????????????????????????????????????????????
"""**55 What is the difference between defaultdict and normal dictionary.**"""
# ******************************************************************************
"""**56 Explain property decorator in python.**"""
# *********************************************************************************
"""**57 What is Mutable and Immutable datatypes.**"""
# *******************************************************************************
"""**58 Explain get() method in dictionaries.**
# ************************************************************************************  
"""
"""**59 Write a list comprehension to get a list of even numbers from 1-50** """

# l = [item for item in range(1, 51) if item % 2 == 0]
# print(l)       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

"""**60 Find the longest non-repeated substring in the below string**"""

# sentence = "python is programming language and programming is fun"
# words = sentence.split()
# l = []
# for word in words:
#     if word not in l:              # ??????????????????????????????????????????????????????????/
#         l.append(word)
#
# res = list(map(l, key=lambda item: len(item)))
# print(res)

"""""**61 Write a program to find the duplicate elements in the list without using inbuilt functions**"""

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# dup = []
# non_dup = []
# for word in names:
#     if word not in non_dup:
#         non_dup.append(word)
#     else:
#         dup.append(word)
#
# print(dup)         # ['apple', 'google', 'yahoo']


"""**62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**"""

# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d = {}
# for word in names:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
#
# print(d)        # {'apple': 2, 'google': 2, 'yahoo': 2, 'facebook': 1, 'gmail': 1}

"""**63 Write a function to check if the number is Prime**

**64 How to create a tuple of numbers from 0 to 10 using range function**"""

"""**65 Write a program to find the largest number in the list without using any inbuilt functions**"""

# l = [10, 9, 55, 44, 345, 756, 844, 888, 999, 3, 4]
# res = sorted(l)
# print(res)  # [3, 4, 9, 10, 44, 55, 345, 756, 844, 888, 999]
# print(res[-1]) # 999

"""**66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.**

**67 Write a program to find most common words in a given list.**
    words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
    'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
    ]

**68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**

**69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.**

**70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**"""
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

"""**71 Write a program to count the number of occurrences of each word in a file.**"""

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# d = {}
# with open(path) as file:
#      for line in file:
#           words = line.split()
#           for word in words:
#                if word not in d:
#                    d[word] = 1
#                else:
#                    d[word] += 1
#
# print(d)    # {'hello': 6, 'world': 4, 'Apple': 1, 'a': 1, 'day,': 1, 'keeps': 1, 'doctor': 1, 'away': 1, 'universe': 1, 'python': 2, 'I': 1, 'am': 1, 'John': 1, 'programming': 1, 'in': 1, 'is': 2, 'fun': 2, 'java': 1}


"""**72 Write a program to count the number of occurrences of vowels in a file.**"""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# d = {}
# with open(path) as file:
#      for line in file:
#           i


"""**73 Write a program to print all numeric values in a list**"""

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for word in items:
#      if isinstance(word, (float, int, float)):
#           print(word, end=" ")    # 1.2 26

"""**74 Triangle Patterns**"""

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(6):
#      print("* "*i)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# a = 10
# for i in range(6):
#      print(" "*a, "* "*i)
#      a -= 2

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5, 0, -1):
#      print("* "*i)

"""
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *

 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
"""
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#      for j in range(1, i+1):
#           print(j, end=" ")
#
#      print("\n")


"""
    1
   12
  123
 1234
12345

     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5


**75 Write a program count the occurrence of a particular word in the file**

**76 Write a program to map a product to a company and build a dictionary with company and list of products pair**
    >>> all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', iOS', 'Google Drive', 'One Drive']

    >>> # Pre-defined products for different companies
    >>> apple_products = {'iPhone', 'Mac', 'iWatch'}
    >>> google_products = {'Gmail', 'Maps', 'Google Drive'}
    >>> msft_products = {'Windows', 'One Drive'}

**77 Write a program to rotate items of the list**
     names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

**78 Write a program to rotate characters in a string**

**79 Write a program to count the number of white spaces in a given string**"""

# s = "hello how are you"
# count = 0
# for i in s:
#      if i == " ":
#           count += 1
#
# print(count)            # 3


"""**80 Write a program to print only non-repeated characters in a string**"""

# s = "hello world how are you"
# non_rep = []
# dub = []
# for i in s:
#      if s.count(i) == 1:
#           non_rep.append(i)
#      else:
#           dub.append(i)
#
# print(non_rep)      # ['d', 'a', 'y', 'u']

"""**81 What is the difference between a list and a tuple**"""
# ***********************************************************************
"""**82 Write a program to print all the consonants in a given string**"""

# s = "hello world how are you"
# for char in s:
#      if char not in "aeiouAEIOU":
#           print(char, end=" ")            # h l l   w r l d   h w   r   y

"""**83 Write a program to count the number of commented lines in a text file**"""
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""**84 Write a program to check if the year is leap year or not**"""
# year = int(input("enter year"))
#
# if year % 4 == 0 or year % 400 == 0:
#     print("leap year")
# else:
#     print("Not leap year")


"""**85 Linear Search**"""
# *******************************************************************************
"""**86 Difference between xrange and range**"""
# ***********************************************************************************
"""**87 Write a program to count no of capital letters in a string**"""

# s = "hEllO WorlD HoW aRe YoU"
# count = 0
# for i in s:
#      if i.isupper():
#           count += 1
#
# print(count) # 9


"""**88 Write a program to get the below output**"""
"""
*
* *
*
* * *
*
* * * *
*
* * * * *
"""
"""**89 Write a program to get the below output**"""
"""
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
o/p:
>>> [1, 2]
    [3, 4]
    [5, 6]
    [7, 8]
    [9]
"""
"""**90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**"""
#
# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# # c = [0, 5, 10, 15]
# # d = [20, 25, 30, 35, 40]
# #
# # x = [10, 20, 30, 40]
# # y = [50, 40, 60, 70]
#
# def series_(l1, l2):
#      res = l[1]-l[0]
#      l3 = []
#      l3 = l1+l2
#      print(l3)
#
# series_(a, b)



"""**91 What is the difference between append() and extend() method in list**"""

"""**92 Write a program to find the first repeating character in a string**"""

"""**93 Write a program to find the index of nth occurrence of a sub-string in a string** 
    >>> sentence = "hello world welcome to python hello hi how are you hello there"
    >>> index_nth_occurance(sentence, 'hello', 3)
    >>> Start Index: 51, End Index: 56

**94 Write a program to print prime numbers from 1 to 50**

**95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order**
     a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
     o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]

**96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should be in ascending order and even numbers should be in descending order**
     a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
     o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]

**97 Write a program to count the number of occurrences of non-special characters in a given string**
     s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

**98 Grouping Flowers and Animals in the below list**
     items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

**99 Grouping files with same extensions**
     files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

**100 Filter only those characters except digits**
      s = '@hello12world34welcome!123'


**101 Count number of words in a sentence. ignore special characters.**
      sentence = "Hi there! How are you:) How are you doing today!"

**102 Grouping even and odd numbers**
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}

**103 Find all max numbers from the below list**
      numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]

**104 Find all max length words from the below sentence**
      sentence = "hello world hi apple you yahoo to you"

**105 Find the range from the following string**
      sentence = '0-0, 4-8, 20-20, 43-45'
      Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]

**106 Can we override a static method in python?**

**107 Write a function which returns the sum of lengths of all the iterables**
      total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2})
      O/p: 15

**108 Replace whitespaces with newline character in the below string**
      sentence = "Hello world welcome to python"

**109 Replace all vowels with "*"
      sentence = "hello world welcome to python"

**110 Replace all occurances of "Java" with "Python" in a file**

**111 Maximum sum of 3 numbers and Minimum sum of 3 numbers**
      numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]

**112 Write a program to get the output as below**"""
# i/p is "python@#$%pool"
# o/p should be ['PYTHON', 'POOL'] 
# s = "python@#$%pool"
# l1 = []
# l = s.split("@#$%")
# for i in l:
#     l1.append(i.upper())
#
#
# print(l1)

"""**113 Write a program to print all the number which are ending with 5**"""

# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# for i in numbers:
#      if int(i[-1]) == 5:
#           print(i, end=" ")      # 12345 125 905 55 5 95655 55555


"""**114 Write a program to get the indexes of each item in the below list**"""
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}





"""**115 Write a program to print "Bangalore" 10 times without using "for" loop any loop **"""

# print("Banglore \n"*10)

"""**116 Write a program to print all the words which starts with letter 'h' in the given string**"""

# string = 'hello world hi hello universe how are you happy birthday'
# words = string.split()
# for word in words:
#     if word[0] == "h":
#         print(word, end=" ")             # hello hi hello how happy


"""**117 Write a program to sum all even numbers in the given string**"""

# sentence = 'hello 123 world 567 welcome to 9724 python'
# s = 0
# for char in sentence:
#     if char.isdigit():
#         if int(char) % 2 == 0:
#             s += int(char)
# print(s)      # 14

"""**118 Write a program to add each number in word1 to number in word2**
    word1 = 'hello 1 2 3 4 5'
    word2 = 'world 5 6 7 8 9'
    # e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9

**119 Write a program to filter out even and odd numbers in the given string**
      sentence = 'hello 123 world 456 welcome to python498675634'

**120 Write a program to print all the number which are starting with 8**"""

# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
#
# for word in numbers:
#     if word[0] == "8":
#         print(word, end=" ")    # 857 8 888888 89

"""**121 Write a program to remove duplicates from the list without using set or empty list**
    l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]

**122 Print all the missing numbers from 1 to 10 in the below list**

**123 Write a python program to get the below output**"""

# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b',
# l3 = []
#
# for  i in l1:
#      for j in l2:
#           l3.append(str(i)+j)
#
# print(l3)      # ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

"""**124 Write a python program to get the below output**

**125 What is the output of the below function call**"""

# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")             # hello universe
#
# d = Demo()
# d.greet()

"""**126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
      a = [3, 5, -4, 8, 11, 1, -1, 6]

**127 Write a decorator to prefix +91 to the original phone numbers**

**128 Write a program to get the below output**
      d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
      o/p should be ['b', 'd']

**129 Can we have multiple __init__ methods in a class**
# *****************************************************************************
**130 Why python is Object Oriented**

**131 What are .pyc files**
"""
##############################################################################
# find / print the second highest value:

# d = {"a": 10, "b": 20, "c": 40, "d": 30}
# l = lambda item: len(item[-1])
# res = list(map(l, d.items()))
#
# *rest, second_max, max_ = res
# print(second_max)

#########################################################
# a = 1
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(a, end=" ")
#         a += 1
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# *********************************************************************************************************************************************************


# SWAP 2 VALUE WITHOUT USING 3RD VARIABLE

# 1. method
# a = 10
# b = 20
# a, b = b, a
# print(a, b)

# 2. method
# a = 10
# b = 20
# b = b - a
# a = a + b
# print(a, b)

# ..........with using 3rd variable ..................

# a = 33
# b = 44
# c =0
#
# c = a
# a = b
# b = c
# print(a,b)

######################################################################################

# find largest 2nd value / runner up value

# a = [10,20,30,30]
#
# # Method 1:
# res = []
# for i in a:
#     if i not in res:
#         res.append(i)
# res.sort()                          # don't be use    x = res.sort()
# print(f"second largest no {res[-2]}")
# print(f"third largest no {res[-3]}")
# print(f"second least no {res[1]}")
# print(res)
#
#
# # method 2:
# res = list(set(a))
# res.sort()
# print(f"second largest no {res[-2]}")
# print(f"third largest no {res[-3]}")
# print(f"second least no {res[1]}")

###################################################
# output = {b:20}

# x = {"a": 10, "b": 20, "c": 30, "d": 30, "e":300}
#
# from collections import defaultdict
# a = defaultdict()
# for key, value in x.items():
#     if x[key] not in a.values():
#         a[key] = value
# print(f'Non duplicate dictionary {a}')
# res = sorted(a.items(), key=lambda item: item[1])
# print(f'second highest value {res[-2]}')
#
#

