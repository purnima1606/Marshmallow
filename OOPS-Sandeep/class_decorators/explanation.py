# function decorating other functions
def log(func):
    def wrapper(*args, **kwargs):
        print("Logging")
        return func(*args, **kwargs)
    return wrapper


@log        # add = log(add)
def add(a, b):
    return a + b


@log        # sub = log(sub)
def sub(a, b):
    return a - b

###################################################################################################
# decorating a function with a class decorator
class Log:
    def __init__(self, func):
        self.func = func

    # wrapper function
    def __call__(self, *args, **kwargs):
        print("logging")
        return self.func(*args, **kwargs)


@Log    # add = Log(add)
def add(a, b):
    return a + b

######################################################################################################
# decorating an entire class with a function decorator

def attach_count(cls):
    cls.count = 0   # Demo.count = 0
    return cls      # return Demo


@attach_count       # Demo = attach_count(Demo)
class Demo:
    def spam(self):
        Demo.count += 1
        print("")

######################################################################################################


























