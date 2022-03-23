def spam(a,b):
    c = a + b
    return c


print(spam(1, 2))       # 3


# positional arguments

def display(name, age):
    print(f"my name is {name} , i am {age} year old")


display("john", 30)      # my name is john , i am 30 year
display(30, "john")      # my name is 30 , i am john year old

# keyword arguments
display(name="john", age=30)   # my name is john , i am 30 year old

# combination of keyword and positional arguments
display("john", age=30)

# positional only arguments

def add(a, b, c, /):
    print(a+b+c)

add(1, 2, 3)           # 6
add( a=1, b=2, c=3)     # typeerror
add( 1, b=2 ,c=3)        # typeerror

def add (a, b, c, /,d):
    print(a+b+c+d)

add(1,2,3,4)
add(1,2,3,d=4)

# keyword only arguments

def add(*,a,b,c):
    print(a+b+c)

add(1 ,2 ,3)      # type error
add(a=1, b=2, c=3)         # 6
add(1, b=2, c=3)         # type error

def add(a, *, b, c):
    print(a+b+c)


add(1, b=2, c=3)
add(a=1, b=2, c=3)

# combination of keyword only and positional only arguments/parameters .

def add(a,b,/,*,c,d):
    print(a+b+c+d)

add(1, 2, c=3, d=4)   # 10

"""~~~~~~~~~~~~~~~~ DEFAULT VALUE ~~~~~~~~~~~~~~~~~~~~~"""

# default parameters .
def add(a, b, c, d=0):
    print(a+b+c+d)

add(1, 2, 3)        # 6
add(1, 2, 3, 4)     # 6

# default value cannot be initialized twice .
a=7
def spam(x=a):
    print(x)

a=10
spam()         # 7
spam(a)        # 10

# variable positional arguments .
def add(*args):
    print(args)
    print(sum(args))

add(1,2,3,4,5,6,7,8)
add()

# variable keyword arguments .

def display(**kwargs):
    print(kwargs)


display(a=1, b=2, c=3)

# combination of variable positional and keyword arguments
def display(*args,**kwargs):
    print(args, kwargs)

display(1,4,5,a=5,b=6,c=7)


"""~~~~~~~~~~~~~~~~~ FUNCTION ANNOTATION'S ~~~~~~~~~~~~~~~~~~~~~~~~~~"""
def add(a:int, b=int)--> int:





