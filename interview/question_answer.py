""" ** 1. Write a program to find the length of the string without using inbuilt function (len) **"""
# string_ = "hello how are you"
# count = 0
# for char in string_:
#     count += 1
# print(count)                   # 17
# print(len(string_))            # 17

""" **2. Write a program to reverse a string without using any inbuilt functions.**"""
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
# print(s.replace("Hello World", "universe"))      # universe

"""**4. How to convert a string to a list and vice-versa.**"""
# s = "hi how are you"
# # string to list
# list_ = s.split()
# print(list_)
# # list to string
# s1 = " ".join(list_)
# print(s1)

"""**5. Convert the string "Hello welcome to Python" to a comma separated string.**"""
# s = "Hello welcome to python"
# l = s.split()
# res = ",".join(l)
# print(res)            # Hello,welcome,to,python

"""**6. Write a program to print alternate characters in a string.**"""
# s = "hi how are you"
# print(s[::2])   # h o r o

"""**7. Write a Program to print ascii values of the characters present in a string.**"""
# s = "programming is fun"
# for char in s:
#     print(char, ord(char))

"""**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**"""
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
# a, b = 10, 20
# print(a, b)
# a, b = 20, 10
# print(a, b)

"""**10. Write a program to merge two different lists.**"""
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [*l1, *l2]
# print(l3)    # [1, 2, 3, 4, 5, 6]
"""**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**"""
# islice


"""**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**

**13 Program to print the last "N" lines of a file.**"""

"""**14. Write a program to check if the given string is Palindrome or not without using reversed method.**"""
# s = "radar"
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


"""**17 Write a to replace all the characters with - if the character occurs more than once in a string**
     my_string = 'hellohai' # O/P should be '-e--o-ai'           # ****************

"""
"""**18 write a decorator that returns only positive values of subtraction**"""

# def decor(func):
#     def wrapper(*args, **kwargs):
#         return abs(func(*args, **kwargs))
#     return wrapper
#
# @decor
# def sub(a, b):
#     return a - b


# print(sub(2, 3))     # 1

"""**19 How to get the count of number of instances of a class that is being created.**


**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer of float it should reverse it.**

**21 Write a class named Simple and it should have iteration capability.**

**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**

**23 Write a python program to get the below output**
     sentence = "Hi How are you"
     o/p should be "iH woH era uoy"

**24 Write a python program to get the below output**
     sentence = "Hi How are you"
     o/p should be "ouy era woH iH"
"""
"""**25 Write a lambda function to add two numbers (a, b)**"""
# l = lambda a, b: a+b
# print(l(2, 3))       # 5

"""**26 What is the output of the following**
    a = [1, 2, 3]
    b = [4, 5, 6]
    print([a, b])
    print((a, b))

**27 How to remove duplicates from the list without using inbuilt functions**
     items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

**28 Find the longest word in the sentence**

**29 write a program to reverse the values in the dictionary if the value is of type String**
     d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

**30 write a program to get 1234"""
# t = ('1', '2', '3', '4')
# res = "".join(t)
# print(int(res))    # 1234

"""
**31 How to get the elements that are in list b but not in list a**
    a = [1, 2, 3]
    b = [1, 2, 3, 4]

**32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**

**33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# Assume Below is the contents of the log file
"""
lines = """CRITICAL:Hello world
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
"""
**34 Write a function to reverse any iterable without using reverse function.

**35 Write a function to print the below output.**
     # func("TRACXN", 0)  # Should print RCN
     # func("TRACXN", 1)  # Should print TAX

**36 Sum all the numbers in the below string.**
     s = "Sony12India567Pvt2ltd"

**37 Write a program to sum all the numbers in below string.**
     s = "Sony12India567Pvt2ltd" # eg.12+567+2

**38 Print all the numbers in the below list**
     a = ['abc', '123', 'hello', '23']

**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**

**40 Program to print only the repeated characters and count of the same.**

**41 Write a program to get alternate characters of a string in list format.**

**42 Write a program to get square of list of number's using lambda function .**

**43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**

**44 Write a program to iterate through list and build a new list, only if the items of the list has even number of characters.**
     names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

**45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.**
     names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']

**46 Write a program which squares the numbers in a list using map object**
     a = [1, 2, 3, 4, 5]

**47 Count number of lines in a file without loading the file to the memory**

**48 Printing line and line no's**

**49 Write a Program to print the sum of entire list and sum of only internal list**
     l = [[1,2,3],[4,5,6],[7,8,9]]

**50 Write a program to reverse the list as below**
     words = ["hi", "hello", "python"]

**51 Write a program to update the tuple**
    t1 = (1, 2, 3, 4)
    t2 = (100, 200, 300)
    # o/p (1, 2, 3, 4, 100, 200, 300)

**52 Write a program to replace value present in nested dictionary.**
    d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
    # Replace "nose" with "net"

**53 Write a program to count the number of white spaces in a file.**

**54 Grouping anagrams.**

**55 What is the difference between defaultdict and normal dictionary.**

**56 Explain property decorator in python.**

**57 What is Mutable and Immutable datatypes.**

**58 Explain get() method in dictionaries.**

**59 Write a list comprehension to get a list of even numbers from 1-50**

**60 Find the longest non-repeated substring in the below string**

**61 Write a program to find the duplicate elements in the list without using inbuilt functions**

**62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
     names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

**63 Write a function to check if the number is Prime**

**64 How to create a tuple of numbers from 0 to 10 using range function**

**65 Write a program to find the largest number in the list without using any inbuilt functions**

**66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.**

**67 Write a program to find most common words in a given list.**
    words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
    'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
    ]

**68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**

**69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.**

**70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
     names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

**71 Write a program to count the number of occurrences of each word in a file.**

**72 Write a program to count the number of occurrences of vowels in a file.**

**73 Write a program to print all numeric values in a list**
     items = ['apple', 1.2, 'google', '12.6', 26, '100']

**74 Triangle Patterns**

*
* *
* * *
* * * *
* * * * *

        *
      * *
    * * *
  * * * *
* * * * *

    *
   * *
  * * *
 * * * *
* * * * *

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

 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *

1
12
123
1234
12345

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

**79 Write a program to count the number of white spaces in a given string**

**80 Write a program to print only non-repeated characters in a string**

**81 What is the difference between a list and a tuple**

**82 Write a program to print all the consonants in a given string**

**83 Write a program to count the number of commented lines in a text file**

**84 Write a program to check if the year is leap year or not**

**85 Linear Search**

**86 Difference between xrange and range**

**87 Write a program to count no of capital letters in a string**

**88 Write a program to get the below output**

*
* *
*
* * *
*
* * * *
*
* * * * *

**89 Write a program to get the below output**

>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
o/p:
>>> [1, 2]
    [3, 4]
    [5, 6]
    [7, 8]
    [9]

**90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**

    a = [10, 12, 14, 16, 18]
    b = [20, 22, 24, 26, 28]

    a = [0, 5, 10, 15]
    b = [20, 25, 30, 35, 40]

    x = [10, 20, 30, 40]
    y = [50, 40, 60, 70]

**91 What is the difference between append() and extend() method in list**

**92 Write a program to find the first repeating character in a string**

**93 Write a program to find the index of nth occurrence of a sub-string in a string**
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

**112 Write a program to get the output as below**
      i/p is "python@#$%pool"
      o/p should be ['PYTHON', 'POOL']

**113 Write a program to print all the number which are ending with 5**
      numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']

**114 Write a program to get the indexes of each item in the below list**
    names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
    output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}

**115 Write a program to print "Bangalore" 10 times without using "for" loop**

**116 Write a program to print all the words which starts with letter 'h' in the given string**
      string = 'hello world hi hello universe how are you happy birthday'

**117 Write a program to sum all even numbers in the given string**
      sentence = 'hello 123 world 567 welcome to 9724 python'

**118 Write a program to add each number in word1 to number in word2**
    word1 = 'hello 1 2 3 4 5'
    word2 = 'world 5 6 7 8 9'
    # e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9

**119 Write a program to filter out even and odd numbers in the given string**
      sentence = 'hello 123 world 456 welcome to python498675634'

**120 Write a program to print all the number which are starting with 8**
      numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']

**121 Write a program to remove duplicates from the list without using set or empty list**
    l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]

**122 Print all the missing numbers from 1 to 10 in the below list**

**123 Write a python program to get the below output**
    >>> l1 = [1, 2, 3]
    >>> l2 = ['a', 'b', 'c']
    >>> # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

**124 Write a python program to get the below output**

**125 What is the output of the below function call**
    class Demo:
        def greet(self):
            print("hello world")

        def greet(self):
            print("hello universe")

    >>> d = Demo()
    >>> d.greet()

**126 In the list below, find all the number pairs which results in 10 either when added or subtracted**
      a = [3, 5, -4, 8, 11, 1, -1, 6]

**127 Write a decorator to prefix +91 to the original phone numbers**

**128 Write a program to get the below output**
      d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
      o/p should be ['b', 'd']

**129 Can we have multiple __init__ methods in a class**

**130 Why python is Object Oriented**

**131 What are .pyc files**
"""
