                                         #  List Programs: 30.Q
""" Python program to interchange first and last elements in a list """
# l = [1,2,3,4,5,6,7,8,9]
# print(l)
# l[0], l[-1] = l[-1], l[0]
# print(l)


""" Python program to swap two elements in a list """
# l = [2,4,6,8]
# print(l)
# l[0], l[1] = l[1], l[0]
# print(l)


""" Python | Ways to find length of list """
# l = [1,2,3,4,5,6,7,8,9]
# # method 1:
# count_ = 0
# for _ in range(len(l)):
#     count_ += 1
# print(count_)
#
# # method 2:
# print(len(l))

""" Python | Ways to check if element exists in list"""
# #  method 1
# l = [2,3,4,5,6,7,8]
# n = int(input("enter which number u want to find in list(l):"))
# for i in l:
#     if n == i:
#         print("element is present inside l:")
#         break
# else:
#     print("element is not present inside l:")

""" Different ways to clear a list in Python"""

l = [3, 6, 9, 12, 15, 18, 21, 24, 27]
# method 1:
for i in l:
    l.remove(i)

print(l)

# # method 2:
# l.clear()
# print(l)

"""Python | Reversing a List"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # method 1
# for i in reversed(l):
#     print(i, end=" ")

# # method 2
# print(l[-1: :-1])

# # method 3
# res = []
# for i in l:
#     res = [i] +res
# print(res)

"""Python program to find sum of elements in list"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # method 1:
# s = 0
# for i in l:
#     s += i
# print(s)
#
# # method 2:
# print(sum(l))


""" Python | Multiply all numbers in the list"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = 1
# for i in l:
#     res *= i
# print(res)


""" Python program to find smallest number in a list"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # method 1:
# min_ = l[-1]
# for i in l:
#     if i < min_:
#         min_ = i
#
# print(min_)
#
# # method 2:
# print(min(l))

""" Python program to find largest number in a list """

# l = [1,2,3,4,5]
# # method 1:
# print(max(l))
#
# # method 2:
# max_ = l[-1]
# for i in l:
#     if i > max_:
#         max_ = i
# print(max_)

""" Python program to find second largest number in a list"""


"""Python program to find N largest elements from a list"""


"""Python program to print even numbers in a list"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in l:
#     if i % 2 == 0:
#         print(i, end=" ")


""" Python program to print odd numbers in a List"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in l:
#     if i % 2 != 0:
#         print(i, end=" ")


""" Python program to print all even numbers in a range"""

# for i in range(20+1):
#     if i % 2 == 0:
#         print(i, end=" ")

"""Python program to print all odd numbers in a range"""

# for i in range(20+1):
#     if i % 2 != 0:
#         print(i, end=" ")

""" Python program to print positive numbers in a list """

# l =[1, 3, 6, 8, 7, -5, -4, -1, -8]
# for i in l:
#     if abs(i) == i:
#         print(i, end=" ")

""" Python program to print negative numbers in a list """

# l = [-22, -6, -4, -8, -33, 44, 66, 2, 7, 5, 3, 6, 4, 1]
# for i in l:
#     if abs(i) != i:
#         print(i, end=" ")

""" Python program to print all positive numbers in a range """
# for i in range(-11, 20):
#     if abs(i) == i:
#         print(i, end=" ")

""" Python program to print all negative numbers in a range """
# for i in range(-11, 20):
#     if abs(i) != i:
#         print(i, end =" ")

""" Remove multiple elements from a list in Python """
# l = [1,2,3,4,5,1,2,3,4,5]
# # method 1:
# res = []
# for i in l:
#     if i not in res:
#         res.append(i)
# print(res)
#
# # method 2: if order is not matter:
# print(list(set(l)))


""" Python – Remove empty List from List"""


""" Python | Cloning or Copying a list """

# l = [1, 2, 3, 4, 5, 6]
# # method 2:
# l1 = l
# print(l)
# print(l1)

""" Python | Count occurrences of an element in a list """

# l = [1,2,3,4,5,1,2,3,4,5]
# for i in set(l):
#     print(i,l.count(i))

""" Python | Remove empty tuples from a list """


""" Python | Program to print duplicates from a list of integers """

# l = [1,2,3,4,56,7,8,5,3,5,2,8,9,6,5]
# for i in set(l):
#     if l.count(i) > 1:
#         print(i)


"""Python program to find Cumulative sum of a list"""


"""Python | Sum of number digits in List"""

# l =[11, 22, 33, 44, 55, 66, 77, 88, 99]
#
# for i in l:
#     res = 0
#     j = i
#     while j:
#         a = j % 10
#         res += a
#         j = j//10
#     print(i,res)


""" Break a list into chunks of size N in Python """


""" Python | Sort the values of first list using second list """

