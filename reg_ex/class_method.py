import json


class Demo:
    # Instance Method - instance will be automatically passed
    def spam(self):
        print(self)

    # class method - class reference will be automatically passed
    @classmethod
    def apple(cls):
        print(cls)

#######################################################################################################
class Employee:

    def __init__(self, fname, lname, pay):
        self.lname = lname
        self.fname = fname
        self.pay = pay

    @classmethod        # Alternate constructor
    def from_string(cls, string):
        parts = info.split(",")
        fname, lname, pay = parts
        # return fname, lname, pay
        return cls(fname, lname, pay)   # Employee(fname, lname, pay)

    @classmethod
    def from_json(cls, json_response):
        data = json.loads(json_response)    # deserialization - converting Json string into python object
        fname = data["fname"]
        lname = data["lname"]
        pay = data["pay"]
        return cls(fname, lname, pay)


# string input
info = "steve,jobs,1000"
e = Employee.from_string(info)

# JSON data
info = '{"fname": "steve", "lname": "jobs", "pay": 1000}'
e.from_json(info)

#######################################################################################################

class Point:

    def __init__(self):
        self.records = []

    @classmethod
    def from_file(cls):
        p = cls()
        with open("points.txt") as file:
            for line in file:
                parts = line.split()
                p.records.append((parts[0], parts[1], parts[2]))
        return p

    # calculate the average of x, y, z co-ordinates
    def average(self):
        x_total = y_total = z_total = 0

        for item in self.records:
            x_total += item[0]
            y_total += item[1]
            z_total += item[2]

        return x_total / len(self.records), y_total / len(self.records), z_total / len(self.records)

    # minimum and maximum
    def min_max(self):
        x_ = []
        y_ = []
        z_ = []
        for item in self.records:
            x_.append(item[0])
            y_.append(item[1])
            z_.append(item[2])
        return ("minimum values: ", min(x_), min(y_), min(z_)), \
               ("maximum values: ", max(x_), max(y_), max(z_))


####################################################################################################
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)      # returns an instance of the same class


c = Circle.from_diameter(4)
