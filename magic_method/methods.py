class Spam:
    pass


s = Spam()
# print(dir(s))

""" methods present in spam by default"""
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__']

##############################################################################
names = ["apple", "google", "yahoo"]

# __contains__ : checks if the given element is present in a container or not --> boolean
print("apple" in names)
print(names.__contains__("apple"))

# __getitem__ : gets the element based on the position in any sequences
print(names[0])
print(names.__getitem__(0))

# __len__ : returns length of an object --> integer
print(len(names))
print(names.__len__())

# __setitem__ : sets element at the specified index
names[0] = "microsoft"
names.__setitem__(0, "microsoft")

# __delitem__: deletes specified indexed item
del names[1]
names.__delitem__(1)

# __getattribute__: to access any attributes in a class i.e., when we use
# object.attribute, then this method will be fired

############################################################################
# comparison protocols
a = 10
b = 20

# __lt__
print(a < b)
print(a.__lt__(b))

# __gt__
print(a > b)
print(a.__gt__(b))

# __le__
print(a <= b)
print(a.__le__(b))

# __ge__
print(a >= b)
print(a.__ge__(b))

# __eq__
print(a == b)
print(a.__eq__(b))

# __ne__
print(a != b)
print(a.__ne__(b))





