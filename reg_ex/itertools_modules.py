from itertools import *

n = range(10)

c = count()

# for item in c:
#     print(item)

l = ["ON", "OFF"]

# for item in cycle(l):
#     print(item)

c1 = cycle(l)
# print(list(c1))
# for _ in range(10):
#     print(next(c1))

r = repeat("hai", 5)

for item in r:
    print(item)