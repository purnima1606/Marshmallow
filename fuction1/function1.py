"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  assignment~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """

""" 1 .WAF  to check if the given number is a fibonacci number or not """


# def fibonacci(n):
#     a = 0
#     b = 1
#     while a <= n:
#         if a == n:
#             return f"{n} is member of fibonacci number"
#         else:
#             c = a + b
#             a = b
#             b = c
#         return f'{n} is not a member of fibonacci number'
#
#
#
# print(fibonacci(49))
# print(fibonacci(2))
# print(fibonacci(5))

# print(fibonacci(5))

""" 2 . WAF to return a dictionary of character and it's index pair in the given. """


# method 1
# def dictionary(n):
#     d = {}
#     for i in n:
#         d[i] = n.index(i)
#     return d
#
# print(dictionary("hello how are you:"))

# method 2 ** prefer first **
# def dictionary(n):
#     d = {}
#     for index,item in enumerate(n):
#         d[index] = item
#     return d
#
# print(dictionary("hello how are you:"))


""" 3 . WAF to return a dictionary from two sequence ."""

# def sequence(l1,l2):
#     d = {}
#     for item1, item2 in zip(l1, l2):
#         d[item1] = item2
#     return d
#
#
# print(sequence([1, 2, 3], [4, 5, 6]))

""" 4 . WAF to return to check whether the given string is palindrome or not ."""


# def palindrome(n):
#     if n == n[::-1]:
#         print(f"string {n} is palindrome:")
#     else:
#         print(f"string {n} is not palindrome:")
#
#
# palindrome("radar")

""" 5 . WAF to check if all the strings present in the list are palindrome or not . """

# Method 1:


# def palindrome(string):
#     if string == string[::-1]:
#         return True
#
#
# l = ["dad", "malayalam", "hai"]
# for word in l:
#     if palindrome(word):
#         continue
#     else:
#         return "Not Palindrome"

# def palindrome(sequence):
#     for word in sequence:
#         if word != word[::-1]:
#             print("Given sequence is not a Palindrome")
#             break
#         else:
#             continue
#     return "Given sequence is a Palindrome")
#
#
# # palindrome(["mom", "madam", "civic"])                   # Given sequence is a Palindrome
# palindrome(["dad", "malayalam", "hai"])                 # not given exact output ???????????????????


# Method 2:
# def palindrome(n):
#     count = 0
#     for i in n:
#         if i == i[::-1]:
#             count += 1
#             if count == len(n):
#                 print(f"{n} is palindrome numbers:")
#         else:
#             print(f" {i} is not palindrome numbers:")
#             break
#
#
# print(palindrome(["radar", "hello", "papa", "ram", "mom"]))






def sum_n_numbers(num, total=0):
    if num > 0:
        total += num
        return sum_n_numbers(num - 1, total)
    return total


n = int(input("Enter a number: "))
print(sum_n_numbers(n))
