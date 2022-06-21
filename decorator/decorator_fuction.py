# monkey patching
# def add(a,b):
#     print(a+b)   # 3
#
#
# x = add         # monkey patching
# x(1, 2)
# print(id(x), id(add))          # 2979246197496 2979246197496

########################################################################################################################

# def spam(func):
#     def wrapper(*args, **kwargs):
#         print("decorator function running:")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @spam               # add = spam(add)
# def add(a, b):
#     return a+b
#
#
# print(add(2, 3))    # decorator function running:
#                    # 5

############################################################################################################################
""" WADF to log a msz before executing any function :"""
# delay == log
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)             # add
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def add(a, b):
#     print("Add function running:")    # Add function running:
#     return a+b
#
#
# print(add(4, 5))   # 9

###############################################################################################################################
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def add():
#     print("Add function running: ")
#
# @log
# def sub():
#     print("Sub function running: ")
#
# @log
# def mul():
#     print("Mul function running:")
#
# @log
# def div():
#     print("Div function running:")
#
#
# add()
# sub()
# mul()
# div()

# add
# Add function running:
# sub
# Sub function running:
# mul
# Mul function running:
# div
# Div function running:

#############################################################################################################################
""" WADF which counts the number of parameter given to a function :"""
# method 1

# def parameter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         print(func.__name__)        # add
#         for p in args:
#             count += 1
#         for p in kwargs:
#             count += 1
#         return f" total arguments count = {count}"
#     return wrapper

# method 2
# def parameter(func):            # solve this
#     def wrapper(*args, **kwargs):
#         num = len(args) + len(kwargs)
#         print(f"total numbers of arguments : {num}")
# @parameter
# def add(a,b,c):
#     return a+b+c
#
#
# add(1, 2, 3)    # total arguments count = 3

#############################################################################################################
""" WADF to input 5 second of delay before execution the function :"""
# import time
# def delay(func):
#     def wrapper(*args, **kwargs):
#         print("Wrapper function Running :")
#         time.sleep(5)
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay
# def display():
#     print("In Display: ")
#
#
# display()
############################################################################################################################
""" WADF to calculate execution time of the function :"""
import time
def calculator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        return f"total execution time of the function is {end - start}", f"output of display:{res}"
    return wrapper


@calculator            # string_ = calculator(string_)     # string_ = wrapper
def string_():
    print("String_ function running: ")  # String_ function running:


print(string_())     # ('total execution time of the function is 0.0', 'output of display:None')

########################################################################################################################
""" WADF to execute a function for 3 time :"""
# def _3time(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(1,3):
#             res = func(*args, **kwargs)
#             print(res)
#         return wrapper
#
# @_3time
# def add(a,b):
#     return a+b
#
# add(4,5)

#############################################################################################################################
""" WADF count the numbers of function call of main function """
# count = 0
# def number_funccall(func):
#     def wrapper(*args, **kwargs):
#         global count
#         count += 1
#         res = func(*args, **kwargs)
#         return f"function calls : {count}", f"{res}"
#     return wrapper
#
# @number_funccall
# def add(a,b):
#     return a+b
#
# @number_funccall
# def sub(a,b):
#     return a-b
#
# print(add(3, 4))           # ('function calls : 1', '7')
# print(add(5, 6))           # ('function calls : 2', '11')
# print(sub(5,4)

##################################################################################################################################
""" WADF TO CREATE A DICTIONARY AND EACH FUNCTIONS CALL"""
# def function_call(func):
#     d = {}
#     def wrapper(*args, **kwargs):
#         if func.__name__ not in d:
#             d[func.__name__] = 1
#         else:
#             d[func.__name__] += 1
#         res = func(*args, **kwargs)
#         return d
#     return wrapper
#
# @function_call
# def add(a, b):
#     return a+b
#
#
# @function_call
# def sub(a, b):
#     return a-b
#
#
# print(add(3, 4))
# print(add(5, 6))
# print(sub(5, 3))
# {'add': 1}
# {'add': 2}
# {'sub': 1}

############################################################################################################

# def positive_value(func):
#     def wrapper(*args, **kwargs):
#         return abs(func(*args, **kwargs))
#     return wrapper
#
# @positive_value
# def sub(a, b):
#     return a-b
#
#
# print(sub(4, 6))   # 2
# print(sub(6, 3))   # 3










