path = r"C:\Users\user\PycharmProjects\Marshmallow\file_handling.py\file.py"

# without using context manager
# file = open(path)
# print(file)
# print(file.closed)           # False
# file.close()
# print(file.closed)           # True

# method 2 with using context manager

# with open(path) as file:
#     print(file.closed)        # False
#
#
# print(file.closed)           # True

""" 1."""
# import os
# # os.chdir(r"C:\Users\user\PycharmProjects\Marshmallow\file_handling.py")
# with open ("file.txt") as x:
#     char_count =0
#     for line in x:
#         char_count += len(line)
#
#     print(char_count)
#
# """ 2 ."""
# import os
# with open("file.py"):
#     word_count =0
#     for line in file:
#         words = line.split()
#         word_count += len(words)
#
# print(word_count)
#
# """ 3 ."""
# with open(file.txt):
#     for line in file:
#         if line.strip:
#             if line[0] in "aeiouAEIOU":
#                 print(line)
#
# """ 4 ."""
# with open(file.txt):
#     line_no = 0
#     for line in file:
#         line_no += 1
#         words = line.split()
#         print(line_no, len(words))
#
#
# """ 5 ."""
# with open(file.txt):
#     list_ = list(file)
#     for line in list_[::-1]:
#         print(line)
#
# """ 6. """
# with open("file.txt"):
#     count = 0
#     for _ in file:                                # for line in file:
#         count += 1
#     print(count)
#
# """ 7 ."""
# with open ("file.py"):
#     count =0
#     for line in file:
#         count += len(line.split())-1
#
# print(count)
#
# """"8 ."""
# with open("file.txt"):
#     d = {}
#     for line in file:
#         if line.strip:
#             words = line.split()
#             for word in words:
#                 d[word] = file.count(word)
#
#     print(d)
#
# """ 9 ."""
# with open("file.txt"):
#     d = {}
#     for line in file:
#         if line.strip:
#             words = line.split()
#             for word in words:
#                 if word not in words:
#                     d[word] =1
#                 else:
#                     d[word] += 1
#
# least, *rest, most = sorted(d.items(), key = lambda item:item[0])
# print(most, *rest, least)
#
#
# """" 10 ."""
# with open(file.txt):
#     count = 0
#     for line in file:
#         count += 1
#         if count == n:
#             print(line)
#
#
# # using enumerate
# with open(file.txt):
#     for line_no, line in enumerate(file):
#         if line_no == n:
#             print(line)
#
#
# """ 11 ."""
# with open(file.txt):
#     count = 0
#     for line in file:
#         count +=1
#         if count <= 5:
#             print(line)


""" 12 ."""
form itertool import islice
# using islice()
l = 5
with open("file.txt"):
    lines = islice(file, l)
    for line in lines:
        print(line)


""" 13 ."""
with open("file.txt"):
    lines = islice(file, 3,8)
    for line in lines:
        print(line)

""" 14 ."""
n = 5
with open("file.txt"):
    count = 0
    for line in file:
        count += 1
    file.seek(0)
    lines = islice (file, count-n, count)
    for line in lines:
        print(line)


# 2 method
from collections import deque
n = 2
with open("file.txt"):
    d = deque(file,n)
    for line in d:
        print(line)
