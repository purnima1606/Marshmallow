class Point:

    def __init__(self, *values):
        # self.points = [*values]   # unpacking a tuple in a list
        self.points = []
        for value in values:
            self.points.append(value)

    def __len__(self):
        return len(self.points)    # returns the length of data structure taken

    def __contains__(self, item):
        return item in self.points

    def __getitem__(self, index):
        return self.points[index]   # self.points.__getitem__(index)

    def __setitem__(self, index, value):    # called only while indexing
        if value < 0:
            raise Exception("Only positive values are allowed")
        self.points[index] = value  # self.points.__setitem__(index, item)






