class Sample:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self, name):
        if self.name == name:
            return self.__salary

    def set_salary(self, value):
        raise ValueError("salary cannot be set")


s = Sample("john", 2000)
print(s.get_salary("john"))
print(s._Sample__salary)
