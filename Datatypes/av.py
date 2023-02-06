# from  numpy improt random
#
# arr = random.randint(40, size=(5))
# print(arr)

from random import random, seed, randint
l = []

# seed(9)
for i in range(10):
    value = randint(0,9)
    l.append(value)

print(l)

print(max(l))
print(min(l))
