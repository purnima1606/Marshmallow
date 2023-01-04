""
"""
********************************* flush() ************************************
- The flush() method in Python file handling clears the internal buffer of the file. 
- In Python, files are automatically flushed while closing them. 
- However, a programmer can flush a file before closing it by using the flush() method. 
"""

import csv
class ConsoleLogger:
    def log(self, message):
        print(message)


class TextLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message)
        self.file.write("\n")
        self.file.flush()       # instead of closing the file, we can flush


class CSVLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        writer = csv.writer(self.file)
        words = message.split()
        writer.writerow(words)
        self.file.flush()

"""
class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern

    # partial overriding
    def log(self, message):
        if self.pattern in message:
            super().log(message)


class FilteredTextLogger(TextLogger):
    # partial overriding
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)      # initializing parent class constructor

    def log(self, message):
        if self.pattern in message:  # Extra functionality added in Child class
            super().log(message)    # Original function from parent class


class FilteredCSVLogger(CSVLogger):
    # partial overriding
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)      # initializing parent class constructor

    def log(self, message):
        if self.pattern in message:  # Extra functionality added in Child class
            super().log(message)    # Original function from parent class

"""


# instead of creating  filter classes for each class, create an independent class
class FilteredLogger:

    def __init__(self, pattern):
        self.pattern = pattern

    # partial overriding
    def log(self, message):
        if self.pattern in message:
            super().log(message)


# using multiple inheritance/ mixin class
class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)


class FilteredTextLogger(FilteredLogger, TextLogger):
    def __init__(self, pattern, file):
        FilteredLogger.__init__(self, pattern)
        TextLogger.__init__(self, file)


class FilteredCSVLogger(FilteredLogger, CSVLogger):
    def __init__(self, pattern, file):
        FilteredLogger.__init__(self, pattern)
        CSVLogger.__init__(self, file)


fcl = FilteredConsoleLogger("error")
fcl.log("This is an error message")

f = open("test.txt", "w")
ftl = FilteredTextLogger("warning", f)
ftl.log("This is a warning message")

f = open("test.csv", "w")
fcsv = FilteredCSVLogger("error", f)
fcsv.log("this is a fatal error")
