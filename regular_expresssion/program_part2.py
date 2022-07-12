import re
############################################################################################################

# download_messages = """
# Downloading file archive.zip to downloads folder......
# downloading file image.jpeg to downloads folder....
# downloading file index.xhtml to downloads folder....
# downloading file python.py to downloads folder....
# """
#
# # print(re.findall(r"\.", download_messages))   # ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# # print(len(re.findall(r"\.", download_messages)))           # 21
# # print(re.findall(r"\.[a-zA-Z]+\b", download_messages))        # ['.jpeg', '.xhtml', '.py']
# # print(re.findall(r"\b[a-zA-Z]\.[a-zA-Z]+\b", download_messages))   # []
# print(re.findall(r"\b[A-Za-z]+\.[a-zA-Z]+\b", download_messages))       # ['archive.zip', 'image.jpeg', 'index.xhtml', 'python.py']


######################################################################################################################################

# class solution:
#     def solve(self, A):
#         self.a =A
#         res = []
#         for i in range(len(self.a)):
#             if len(self.a) % 2 == 0:
#                 if i == len(self.a)//2:
#                     res.append(self.a[i])
#             elif i == (len(self.a)//2)+1:
#                 res.append(self.a[i])
#
#
# output = solution()
# print(output.solve([1, 2, 3, 4, 5]))

###########################################################
# a = int(input("enter a number for a:"))
# b = int(input("enter a number for b:"))
#
# if a > b :
#     if a-b == 2:
#         print(b)
# elif b > a:
#     if b-a == 2:
#         print(a)
# else:
#     print("not match")

############################################################################

# for x in range(1, 6):
#     l = []
#     for y in range(1, x+1):
#         l.append(y)
#     print(l)
#     # print()
