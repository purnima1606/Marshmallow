# Arithmetic operator

# print(1 + 2)
# print(1.4 + 7.2)
# print(1+2j + 5+8j)
# print(True + False)
# print([1, 2, 3, 4] + [5, 6, 7])
# print("hai" + "hello")

# subtraction
""" all individual datatypes and sets"""

# multiplication

# print("hai" * 2)
# print([1, 2, 3] * 2)
# print((1, 2, 3) * 2)
# print({1, 2, 3} * 2)

# floor division
#
# print(9 // 2)
# print(9 // -2)

# Relational operator

# print("hai" > "hello")
# print([1, 2, 3] < [2, 3, 4])
# print([1, 2, 4, 5] < [1, 2, 5])
# print({2, 3} == {3, 2})
# print([1, 2, 3] == [3, 2, 1])


# logical operators
# print(10 > 1 and 20 < 50)
# print(10 and 20 and 0)
# print(10 or 20 or 0)
# print(not 9.8)


# print(10 == 20)
# a = 20
# a = a + 1
# a += 1

# identity operator

a = [1, 2, [3]]
b = [1, 2, [3]]   # b = a[::]
# b = a
print(a == b)
print(id(a) == id(b))
print(a is b)
print(a is not b)

s = "hello"
print("a" in s)
print(2 in [1, 2, 3])
print(2 in [1, [2], 3])
print((1, 2) in [1, 2, 3])
print(1, 2 in [1, 2, 3])
print("1" not in "hello")







































