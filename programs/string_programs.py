                                         # String Programs:30.Q

""" Python program to check if a string is palindrome or not"""
# s = input("enter the string:")
# # method 1
# if s == s[::-1]:
#     print("string is palindrome:")
# else:
#     print("string is not palindrome:")

# # method 2:
# res =""
# for i in reversed(s):
#     res += i
#
# if res == s:
#     print("string is palindrome:")
# else:
#     print("string is not palindrome:")

""" Python program to check whether the string is Symmetrical or Palindrome"""
#  same answer

""" Reverse words in a given String in Python """

# s = "python is programming language"
# l = []
# for i in s.split(" "):
#     l.append(i[::-1])
# print(" ".join(l))

""" Ways to remove i’th character from string in Python """

# n = int(input("enter nth position:"))
# s = "python is easy language"
# res = ""
# for index,i in enumerate(s):
#     if index != n:
#         res += i
#     else:
#         continue
#
# print(res)

""" Python | Check if a Substring is Present in a Given String """

# s = "hi hello you mad"
# n = input("enter substring:")
# if n in s:
#     print(f"substring {n} is present in {s}:")
# else:
#     print(f"substring {n} is not present in {s}:")

""" Python – Words Frequency in String Shorthands """

# s = "are you looking for job if yes then you are selected no interview no tension"
# for word in set(s.split()):
#     print(word, s.count(word), end="  ")


""" Python – Convert Snake case to Pascal case """
# snake case = geeks_for_geeks
# pascal case = GeeksforGeeks

# s = "geeks_for_geeks"
# res = s.title()
# print("".join(res.split("_")))

""" Find length of a string in python (4 ways) """

# s = "python is not easy"
#
# # method 1:
# print(len(s))
#
# # method 2:
# count_ = 0
# for i in s:
#     count_ += 1
# print(count_)
#
# # method 3:

""" Python program to print even length words in a string """

# s = "hi how are you can i help yo"
# for i in s.split(" "):
#     if len(i) % 2 == 0:
#         print(i)

""" Python program to accept the strings which contains all vowels """

# s = input("enter all vowel strings:")
# count_ = 0
# for i in s:
#     if i in "aeiouAEIOU":
#
#         count_ += 1
#
# if count_ == len(s):
#     print("the strings which contains all vowels")
# else:
#     print("the strings not contains all vowels")

""" Python | Count the Number of matching characters in a pair of string """
# s = "python is programing language"
# for i in set(s):
#     print(i, s.count(i))


""" Remove all duplicates from a given string in Python """

# s = "hi how are you hi how is your life"
# res = ""
# for word in s.split():
#     if word not in res:
#         res += " " + str(word)
#
# print(res)
#
# # method
# print(set(s.split()))

""" Python – Least Frequent Character in String """
# s = "hi how are you"
# for i in set(s):
#     if s.count(i) == 1:
#         print(i, end=" ")


""" Python | Maximum frequency character in String """


""" Python | Program to check if a string contains any special character """


""" Generating random strings until a given string is generated """


""" Find words which are greater than given length k """


""" Python program for removing i-th character from a string"""


"""Python program to split and join a string"""


"""Python | Check if a given string is binary string or not"""


"""Python program to find uncommon words from two Strings"""

""" Python – Replace duplicate Occurrence in String"""

"""Python – Replace multiple words with K"""

"""Python | Permutation of a given string using inbuilt function """

""" Python | Check for URL in a String """

""" Execute a String of Code in Python"""

"""String slicing in Python to rotate a string """

""" String slicing in Python to check if a string can become empty by recursive deletion """

""" Python Counter| Find all duplicate characters in string """

""" Python – Replace all occurrences of a substring in a string """
