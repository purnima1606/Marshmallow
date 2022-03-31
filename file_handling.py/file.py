""" WAP to get only the Ip address and their count in axis.log.txt: """
import os, csv
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\access-log.txt"
# with open(path)as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             data = line.split()
#             if data[0] not in d:
#                 d[data[0]] = 1
#             else:
#                 d[data[0]] += 1
#     # print(d)
# print(dict(sorted(d.items(), key = lambda item: item[-1])))        # print IP address with count

""" WAP to print the most occurring brand name from data.txt """
# path = r"C:\Users\user\PycharmProjects\Marshmallow\files\data.txt"
# d = {}
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             words = line.strip()
#             for word in words:
#                 if word[0] not in d:
#                     d[word[0]] = 1
#             else:
#                 d[word[[0]]] += 1
#
# min_, *rest, max_ = sorted(d.items(), key = lambda item: item[-1])
# print(max_)                # TypeError: string indices must be integers
#  ::::::::::::::::::::::: 2ND METHOD :::::::::::::::::::
from collections import defaultdict, countor
path = r"C:\Users\user\PycharmProjects\Marshmallow\files\data.txt"
with open(path) as file:
    l = []
    for line in file:
        if line.strip():
            words = line.strip("\t")
            l.append(word[0])

c = countor(l)
print(c)
print(c, most_common(l))
""" 3 """
path = r"C:\Users\user\PycharmProjects\Marshmallow\files\sample.log"
with open(path) as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split("\t")
            for word in words:
                if word[2] not in d:
                    d[word[2]] = 1
                else:
                    d[word[2]] += 1

print(d)
""" 4 """
with open(path) as file:
    print(file)
    dd = defaultdict()






""" WAP to create a dictionary of msz and it's no of occurrence in sample.log.txt: """
