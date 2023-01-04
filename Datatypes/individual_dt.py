""" Integers """
a = 10
b = int(86)

# default value
c = int()
d = 0
# print(a, b, c)

""" float numbers """

a = 10.0
b = float(3.5)

# default value
c = 0.0
d = float()

x = round(3.141672, 3)
# print(x)

y = round(4.8234)
# print(y)


import math
# print(math.trunc(4.8234))

""" complex numbers """

c = 2 + 3j
d = complex(2+3J)
e = complex(2, 3)

# default value

a = 0+0j
b = 0j
c = complex()

""" boolean values """

a = True
b = False

# default value
c = False
d = bool()


""" type() """
# x = 18
# print(type(x))
#
# y = 12.7
# print(type(y))
#
# z = 1+2j
# print(type(z))
#
# n = True
# print(type(n))

""" isinstance() """
x = 18

# print(type(x) == int)
# print(isinstance(x, int))
#
# print(type(x) == float)
# print(isinstance(x, float))
#
# print(isinstance(x, (int, float, complex)))


""" Type casting """

# integer
x = 10

y = float(x)        # 10.0
c = complex(x)      # 10+0j
b = bool(x)         # True


# float
f = 9.8734

print(int(f))       # 9
print(complex(f))   # 9.8734+0j
print(bool(f))      # True

# complex

c = 1+2j
print(int(c))       # TypeError
print(float(c))     # TypeError
print(bool(c))      # True


# boolean
# print(int(True))
# print(int(False))   # 0
#
# print(float(True))
# print(float(False))     # 0.0
#
# print(complex(True))
# print(complex(False))   # 0j

























