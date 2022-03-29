# path = r"C:\Users\user\PycharmProjects\Marshmallow\file_handling.py\file.py"
#
# # without using context manager
# # file = open(path)
# # print(file)
# # print(file.closed)           # False
# # file.close()
# # print(file.closed)           # True
#
# # method 2 with using context manager
#
# # with open(path) as file:
# #     print(file.closed)        # False
# #
# #
# # print(file.closed)           # True
#
# """ 1."""
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     char_count =0
#     for line in file:
#         char_count += len(line)
#
#     print(char_count)              # 160

# # """ 2 ."""
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     word_count = 0
#     for line in file:
#         words = line.split()
#         word_count += len(words)
#
# print(word_count)                # 29

# # """ 3 ."""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     for line in file:
#         if line.strip:
#             if line[0] in "aeiouAEIOU":           # Apple a day, keeps doctor away
#
#                                                    # I am John
#                 print(line)
# #
# # # """ 4 ."""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     line_no = 0
#     for line in file:
#         line_no += 1
#         words = line.split()
#         print(line_no, len(words))          # run


# # """ 5 ."""
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     list_ = list(file)
#     for line in list_[::-1]:
#         print(line)                # print reverse line
# #
# # """ 6. """
# path = r'C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt'
# with open(path) as file:
#     count = 0
#     for _ in file:                                # for line in file:
#         count += 1
#     print(count)       # 10
# #
# # """ 7 ."""
# path = r'C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += len(line.split())-1
#
# print(count)             # 19


# # """"8 ."""

# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip:
#             words = line.split()
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#
#     print(d)   # {'hello': 6, 'world': 4, 'Apple': 1, 'a': 1, 'day,': 1, 'keeps': 1, 'doctor': 1, 'away': 1, 'universe': 1, 'python': 2, 'I': 1, 'am': 1, 'John': 1, 'programming

# # """ 9 ."""
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     print(path)
#     d = {}
#     for line in file:
#         if line.strip:
#             words = line.split()
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#
#
# least, *rest, most = sorted(d.items(), key=lambda item: item[1])
# #print(most, *rest, least)
# # ('hello', 6) ('a', 1) ('day,', 1) ('keeps', 1) ('doctor', 1) ('away', 1) ('universe', 1) ('I', 1) ('am', 1) ('John', 1) ('programming', 1) ('in', 1) ('java', 1) ('python', 2) ('is', 2) ('fun', 2) ('world', 4) ('Apple', 1)
# print(most)   # ('hello', 6)

# # """" 10 ."""
# n = 3
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count == n:
#             print(line)
#

#using enumerate
# n = 4
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         if line_no == n:
#             print(line)

# #
""" 11 ."""
# import os
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count <= 5:
#             print(line)

""" 12 ."""
# from itertools import islice
# # using islice()
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# l = 5
# with open(path) as file:
#     lines = islice(file, l)
#     for line in lines:
#         print(line)                # run


""" 13 ."""
# from itertools import islice
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
# with open(path) as file:
#     lines = islice(file, 3, 8)
#     for line in lines:
#         print(line)          # print lines between 3 to 8

# """ 14 ."""
from itertools import islice
path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.txt"
n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     lines = islice(file, count-n, count)
#     for line in lines:            # print last n line
#         print(line)

    # 2 method
# from collections import deque
# n = 2
# with open(path) as file:
#     d = deque(file, n)
#     for line in d:
#         print(line)              # print last n line
