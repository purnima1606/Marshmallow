""
"""
- Composition is a concept that models a has a relationship. 
- It enables creating complex types by combining objects of other types. 
- This means that a class Composite can contain an object of another class Component . 
- This relationship means that a Composite has a Component .

# method overriding can be seen only in inheritance but not in independent functions.
# method overloading is a feature of polymorphism.
"""

# example of Run-time polymorphism
class ConsoleLogger:
    def log(self, message):
        print(message)


class TextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message+"\n")
        self.file.flush()


# class FilteredConsoleLogger(ConsoleLogger):
#     def __init__(self, pattern):
#         self.pattern = pattern
#
#     def log(self, message):
#         if self.pattern in message:
#             super().log(message)


# class FilteredTextLogger(TextFileLogger):
#     def __init__(self, pattern, file):
#         self.pattern = pattern
#         super().__init__(file)
#
#     def log(self, message):
#         if self.pattern in message:
#             super().log(message)


class FilteredLogger:

    # based on the object passed at the run time, corresponding log method will be called
    def __init__(self, pattern, logger_object):
        self.pattern = pattern
        self.logger_object = logger_object

    def log(self, message):
        if self.pattern in message:
            self.logger_object.log(message)


# passing ConsoleLogger object to FilteredLogger class externally
c = ConsoleLogger()
f = FilteredLogger("error", c)
f.log("This is an error message")

# passing TextFileLogger object to FilteredLogger class externally
file = open("sample.txt", "w")
t = TextFileLogger(file)
f = FilteredLogger("error", t)
f.log("This is an error message")
