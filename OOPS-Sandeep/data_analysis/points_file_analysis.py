# reading 1M records into a python data structure
import tracemalloc


def from_file():
    records = []
    with open("points.txt") as file:
        for line in file:
            parts = line.split()
            # parts = [float(parts[0]), float(parts[1]), float(parts[2])]
            parts = list(map(float, parts))   # mapping float function with parts list
            records.append(parts)
    return records

###################################################################################################
# or creating the list in another function
def make_list(row):
    return [float(row[0]), float(row[1]), float(row[2])]


def from_file():
    records = []
    with open("points.txt") as file:
        for line in file:
            parts = line.split()
            records.append(make_list(parts))
    return records

######################################################################################################
# measuring the memory utilization of the above list of one million records
"""
getsizeof() : returns size/memory of the slots holding the objects address (gives shallow memory allocation)
i.e., if we consider a list then getsizeof() will give the memory of only the number of slots in that list
but not the memory of each slot's object

eg:
from sys import getsizeof

d = {"a": 1, "b": 2}
print(getsizeof(d))     # 232

l = []
l.append(d)
print(getsizeof(l))     # 88

The actual memory utilization of list should be 88 + 232 as it is holding the dictionary object but it 
returns only the list slot's memory. Hence getsizeof() is shallow.

tracemalloc.py 
- python module
- It helps us to trace the memory of any programmable entity completely.
- The drawback of getsizeof() can be overcome using tracemalloc as it gives complete memory utilized by
any object including the objects inside that data.
- get_traced_memory() - returns tuple of lower limit and upper limit

"""

def memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        data = func(*args, **kwargs)
        print(f"Memory utilization: {tracemalloc.get_traced_memory()}")
        tracemalloc.stop()
        return data
    return wrapper


def make_list(row):
    """ creates a list """
    return [float(row[0]), float(row[1]), float(row[2])]

def make_tuple(row):
    """ creates a tuple """
    return [float(row[0]), float(row[1]), float(row[2])]

def make_dictionary(row):
    """ creates a dictionary """
    return {"x": float(row[0]), "y": float(row[1]), "z": float(row[2])}

@memory
def from_file():
    records = []
    with open("points.txt") as file:
        for line in file:
            parts = line.split()
            records.append(make_list(parts))    # ~160 MB
            # records.append(make_tuple(parts)) # ~144 MB
            # records.append(make_dictionary(parts))    # ~ 312 MB
    return records

"""
- Tuples occupy less memory when compared to list. so tuples are more memory efficient than other data 
  structures but to get each value in tuple, we need to index it which is not an efficient way.
- Using dictionary would be the efficient data structure as it do not have indexing and values can be 
  taken directly using their names. But the downside is that it takes more memory.
- So we need to store the records in a dictionary and also make it memory efficient, hence it is better
  to use instance dictionaries instead of normal dictionaries
"""

######################################################################################################
# creating a class to store 1M records (by default it creates instance dictionary)
# representing each record as Point class' instance / storing it in instance dictionary

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def make_instance(row):
    # creates an instance of "Point" class
    return Point(float(row[0]), float(row[1]), float(row[2]))


# @memory
# def from_file():
#     records = []
#     with open("points.txt") as file:
#         for line in file:
#             parts = line.split()
#             records.append(make_instance(parts))
#
#     return records


data = from_file()      # data --> list of records in the form of instance of point class
# each record will be in the form of instance of point class(totally 1 million instances) and
# internally it will be stored as instance dict

# getting x, y, z co-ordinates of first record
# print(data[0].x)
# print(data[0].y)
# print(data[0].z)

# getting x, y, z co-ordinates of nth record
# print(data[n].x)
# print(data[n].y)
# print(data[n].z)

#################################################################################################
# calculate the average of x, y, z co-ordinates
def average():
    x_total = 0
    y_total = 0
    z_total = 0

    data = from_file()
    for item in data:
        x_total += item.x
        y_total += item.y
        z_total += item.z

    return x_total/len(data), y_total/len(data), z_total/len(data)

#####################################################################################################
# minimum and maximum

def min_max():
    x_ = []
    y_ = []
    z_ = []
    data = from_file()

    for item in data:
        x_.append(item.x)
        y_.append(item.y)
        z_.append(item.z)
    return ("minimum values: ", min(x_), min(y_), min(z_)), \
           ("maximum values: ", max(x_), max(y_), max(z_))



























