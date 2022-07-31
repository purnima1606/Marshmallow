
""" Multiples of 3 or 5: Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# n = int(input("entetr the last range number:"))
# sum_ = 0
#
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         sum_ += i
#
# print(sum_)
# # n = 1000 then sum_ = 233168


# -----------------------------------------------------------------------------------------------------------------------------

""" Even Fibonacci numbers:  Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

# sum_, a, b, c = 0, 0, 1, 0
#
# for _ in range(400000):
#     # print(c, end=" ")
#     if c % 2 == 0:
#         sum_ += c
#     a = b
#     b = c
#     c = a + b
#
# print(sum_)


# -----------------------------------------------------------------------------------------------------------------------------------------------------

""" Largest prime factor: Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


# ------------------------------------------------------------------------------------------------------------------------------------------------------
""" Largest palindrome product: Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


# ------------------------------------------------------------------------------------------------------------------------------------------------------
""" Smallest multiple:  Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# a = 20
#
# while True:
#     count_ = 0
#     a += 1
#     for i in range(1,21):
#         if a % i == 0:
#             count_ += 1
#     if count_ == 20:
#         print(a)
#         break




# --------------------------------------------------------------------------------------------------------------------------------------------------------
""" Sum square difference: Problem 6
The sum of the squares of the first ten natural numbers is,
1**2 +2**2 + ...........+ 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2+ .....+10 )**2 = 55**2 =3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# squ_sum = 0
# sum_squ = 0
#
# for i in range(1,101):
#     squ_sum += i
#     sum_squ += i ** 2
#
# squ_sum = squ_sum ** 2
# differece_ = squ_sum - sum_squ
#
# print(differece_)  # 25164150


# -------------------------------------------------------------------------------------------------------------------------------------------------------
""" 10001st prime: Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

# --------------------------------------------------------------------------------------------------------------------------------------------------------
""" Largest product in a series :Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""


# ------------------------------------------------------------------------------------------------------------------------------------------------------------

""" Special Pythagorean triplet: Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# --------------------------------------------------------------------------------------------------------------------------------------------------------
""" Summation of primes: Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million. 
"""
# sum_ = 0
# a = 0
# for i in range(2,200000):
#     for
#     if a % i == 0:
#         break
# else:
#     sum_ +=
#
# print(sum_)
#
#     # if sum_ > 2000:
#     #     print(sum_)
#     #     break










