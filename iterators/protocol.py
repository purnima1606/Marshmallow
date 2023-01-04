l = [1, 2, 3, 4]

# iterable      # __iter__
# for item in l:
#     print(item)

# print(dir(l))

# converting an iterable into iterator object

a = iter(l)
print(a)

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for item in l:
    print(item)


# iterator protocol

a = iter(l)

while True:
    try:
        item = next(a)

    except StopIteration:
        break

    print(item)
















