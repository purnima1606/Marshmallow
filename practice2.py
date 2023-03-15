# wap replace one str with other
# s = "hello"
#
# r = s.replace("hello", "hi")
# print(r)     # hi

# wap to convert the str
# s = "hello welcome to python"
# l = s.split()

########################
# s = "hello"
#
# key = "e"
# r = s.find(key)
# print(r)               # 1
#
# def s_():
#     try:
#         return s.find(key)
#     except Value

############################
#  17 Q.

s = "hello"
# 1. method
# for char in s:
#     if s.count(char) > 1:
#         print("_", end="")
#     else:
#         print(char, end="")

# he__o

# 2. method  using join


# p = "".join(["-" if s.count(char) > 1 else char  for char in s ])
# print(p)      # he--o

# 3. method
# out = ""
# for i in s:
#     if s.count(i) > 1:
#         out += i.replace(i, "-")
#     else:
#         out += i
#
# print(out)   # he--o

#################################################
# interview question............................

s = "({[{{[[]]]]}]}}})"
open_ = 0
close_ = 0
# for i in s:
#     if i == "{" or i == "[" or i == "(":
#         open_ += 1
#     elif i == ")" or i == "}" or i == "]":
#         close_ += 1
#
# if open_ == close_:
#      print("equal")
# else:
#      print("not equal")
# print(open_)
# print(close_)

# 2
#
# for i in s:
#     if i in "[{(":
#         open_ += 1
#     elif i in ")}]":
#         close_ += 1
#
# if open_ == close_:
#      print("equal")
# else:
#      print("not equal")
# print(open_)
# print(close_)






# use list
# use strip

##########################################################

s = "python is good"
# o/p = [(0,5),(7,8),(10,13)]
st = 0
ed = 0
l = []
# for i in s:
#     if i == " ":
#         nx = s.index(" ")+1
#         ed = s.index(" ")-1
#         l.append((st, ed))
#         st = nx
#     else:
#         continue             #   # [(0, 5), (7, 5)]
#



s = "python is good"
# o/p = [(0,5),(7,8),(10,13)]
st = 0
ed = 0
l = []

for i in s:
    if i !=" ":
        ed = s.index(i)
    else:
        nx = s.index(" ")+1
        l.append((st,ed))
        st = nx


print(l)
# [(0, 5), (7, 8)]
# print(len(s))



