class Sample:
    count = 0

    def __init__(self, value1, value2):
        self.a = value1
        self.b = value2
        Sample.count = 1

    def __setattr__(self, key, value):
        if Sample.count == 1:
            raise TypeError("Value cannot be modified")
        else:
            super().__setattr__(key, value)


s = Sample(10, 20)
s.a = 30
print(s.a)
