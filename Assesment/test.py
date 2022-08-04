# all permutations::

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# res = []
#
# for i in range(0,x+1):
#     for j in range(0, y+1):
#         for k in range(0, z+1):
#             if i+j+k != n:
#                 res.append((i, j, k))
#
#
# print(res)


#
# print("1. insert")
# print("2. print")
# print("3. remove")
# print("4. append")
# print("5. sort")
# print("6. pop")
# print("7. reverse")
#
# x = input()
# res = []
#
# for _ in range(5):
#     if x == "1":
#         e = int(input())
#         pos = int(input())
#         res.insert(e, pos)
#         print(res)
#         continue
#     elif x == "2":
#         print(res)
#         continue
#     elif x == "3":
#         e = input()
#         res.remove(e)
#         print(res)
#         continue
#     elif x == "4":
#         e = int(input())
#         res.append(e)
#         print(res)
#         continue
#     elif x == "5":
#         res.sort()
#         print(res)
#         continue
#     elif x == "6":
#         res.pop()
#         print(res)
#         continue
#     elif x == "7":
#         res.reverse()
#         print(res)
#         continue


# if "insert i e" == x:
#     res.insert()



# res = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     res.append([name, score])
#     # res.sort()
#
# print(sorted(res))

# **********************************
# n = "41+(6*(8-5))/4"
# print(eval(n))


# *********************************************************

# n = int(input("enter the value of n:"))
# # binary = 0
# for i in range(1, n+1):
#     o = oct(i)
#     h = hex(i)
#     b = bin(i)
#     print("%6d"%i,o[2:], h[2:], b[2:])
#



#     if 1 <= i <= n:
    #     print(i)
    # if 1 <= i <= 7 or 10 <= i <= 17 or 20 <= i <= 27:
    #     print(i)
    # binary += i//2
    # print( binary)


# p = oct(n)
# # print(type(p))
# print(p[2:])
# # print(bin(n), hex(n))

# ___________________________________________________________________________________________________________________
s = "HelloWorld"
for i in s:
    if "A" <= i <= "Z":
        print(i, end=" ")
