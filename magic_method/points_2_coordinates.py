# making Point object subscriptable
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __len__(self):
        return 2

    def __contains__(self, item):
        return item in self.__dict__.values()

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise Exception("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise IndexError

    def __delitem__(self, key):
        raise Exception()



p1 = Point(1, 2)
print(p1.__dict__)
p2 = Point(1.5, 3.4)

# getting length of object p1
print(len(p1))  # 2

# checking if an element is present in p1
print(1 in p1)  # True

# indexing p1
print(p1[0])    # 1

# setting element in p1
p1[1] = 2.3
print(p1[1])    # 2.3
