# cpunt the elements inside 10-1 .
# def count():
#     i=10
#     if i >= 1:
#         print(i)
#         return count(i-1)

# count()

2.


def rev_count(start , end):
    if start < end:
        return
    print(start)
    rev_count(start-1 ,end)


rev_count(10,1)

 # 3. n= 123 sum =1+2+3
# sum = 0
# n = 123
# while n !=0:
#     sum = sum +(n %10)
#     n= n//10
#
# print(sum)           # 6
# using recursion:

# def rec(n,s=0):
#     if n == 0:
#         return s
#     else:
#         s = s+(n%10)
#         return rec(n//10,s)
#
#
# print(rec(123))                  # 6

# 4 .

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibo(n-1) + fibo(n-2))

# n = 5
# if n <= 0:
#     "invalid"
# else:
#     for i in range(n):
#         print(fibo(i))
#
#
# #print(fibo(5))

############################
# 1 .
# sentence = "it is a very good book and reading book is a good habit"
# def cre_dit(sentence):
#     x = sentence.split()
#     d = {}
#     for i in set(x):
#         d[i] = sentence.count(i)
#     return d
#
#                                                 # 2
# print(cre_dit(sentence))

## 2 .
# a = ["hai", "guys", "welcome", "to", "my", "chanel"]
#
#
# def count_(n):
#     count = 0
#     for i in n:
#         count += 1
#     print(count)            # 6
#
#
# count_(a)


# 3.
# b = "please like share and saparakaribe"
#
#
# def st_vow(n):
#     x = n.split()
#     l = []
#     for i in x:
#         if i[0] in "aeiouAEIOU":
#             l.append(i)
#     return l
#
#                          # 2
# print(st_vow(b))


# 4 .6
# def rev(n):
#     res = ""
#     for i in n:
#         res = i + res
#     return res                       # 2
#
#
# print(rev("hello"))


# 5 . # 8
# s = "Don't foRGet to Press the bell Icom"
#
#
# def convert(n):
#     res = ""
#     for i in n:
#         if "a" <= i <= "z":
#             res = res + chr(ord(i)-32)
#         elif "A" <= i <= "Z":
#             res = res + chr(ord(i)+32)
#         else:
#             res = res + i                       # 2
#     return res
#
#
# print(convert(s))

# 6. #9
# s = "hello"
#
#
# def first_l_m(string):
#     print(string[0])
#     print(string[-1])
#     x = len(string)//2                             # 1
#     print(string[x],string[x+1])
#
#
# first_l_m(s)

# 7 .# 10
# a = int (input("enter the value"))
#
#
# def series(n):
#     a = 0
#     b = 1
#     while a <= n:
#         print(a, end="")
#         c = a+b
#         a = b
#         b = c              # 1
#
# print(series(a))
# 8 # 4
# num =12
#
# def prime_(num):
#     count = 0
#     for i in range(2, num//2+1):
#         if num%i == 0:
#             count += 1
#     if count>0:
#         print("not prime")
#     else:
#         print("no is number 0")
#
#
#  print(prime_(num))

# 9 . 5
# n = 10
#
#
# def fibo(n):
#     count = 2
#     a = 0
#     b = 1
#     i = 0
#     while i<n:
#         if n == count:
#             return c
#         else:
#             c = a+ b
#             count += 1
#         i += 1
#
#
# print(fibo(n))

