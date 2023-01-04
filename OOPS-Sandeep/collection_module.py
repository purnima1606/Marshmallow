# namedtuple
from collections import *

n = namedtuple("n", ["x", "y", "z"])

def create_namedtuple():
    return n(10, 20, 30)


# dataclasses

from dataclasses import dataclass


class Spam:

    def __init__(self, name, age):
        self.name = name
        self.age = age


@dataclass
class Spam1:

    name: str
    age: int

###########################################################################################

d = {"a": 1, "b": 2}
print(d)

d["c"] = 3
print(d)

d["a"] = 10
print(d)
del d["a"]

print(d)
d["a"] = 10
print(d)


# od = OrderedDict()
#
# od["a"] = 10
# print(od)
# od["b"] = 20
# print(od)
# od["c"] = 30
# print(od)
# od["a"] += 18
# print(od)












