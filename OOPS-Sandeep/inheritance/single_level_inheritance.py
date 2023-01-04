""
"""
* Inheritance - deriving the properties of one class to another to modify the other class
* All the attributes will be inherited by the Child class

            Parent
               ^
               |
               |
            class
"""

class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print(f"Executing Parent Apple {self.value}")

    def google(self):
        print(f"Executing Parent Google")
        self.apple()    # apple() is an instance method so if we need to use it anywhere
        # inside class then it should be called with object's address(self)


""" *********************** Single Inheritance **************************** """
# Child class with independent method
class Child1(Parent):

    # independent method in Child1
    def yahoo(self):
        print("Executing Child1 Yahoo")

c= Child1(17)

############################################################################################
"""
* Even if the Child1 class do not have constructor of its own, as it is inheriting from the Parent
class, it can access the parent class constructor.
* If there are constructors in both Parent as well as Child classes, then Child can access only its
constructor.
* In order to call parent class constructor, child class can have super()
* we can have constructor in Child class when there are independent variables which are specific
to Parent class
"""
##########################################################################################
# Single inheritance with method overriding
"""
* constructor chaining - calling Parent class __init__ or calling parent class __init__
* method chaining - calling Pare class methods pr calling any methods of parent class
"""

# Constructor chaining
class Child1(Parent):

    def __init__(self, value): # overriding parent class constructor
        super().__init__(value) # super() is used to access parent class attribute
        # Parent.__init__(self, value)

    # independent method in Child1
    def yahoo(self):
        print("Executing Child1 Yahoo")

c= Child1(17)

#########################################################################################
""" Single Inheritance with method overriding  """

# completely overriding apple()
class Child2(Parent):

    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Running Child2 Apple")

c2 = Child2(20)

##########################################################################################
"""         Single inheritance with method chaining 
* redefining a method in child class and giving extra functionality along
* with parent class functionality
"""

# partial overriding - adding additional functionality along with parent class's
# functionality
class Child3(Parent):

    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Executing Child3 apple method")      # Extra functionality
        super().apple()     # reusing parent class apple method


c3 = Child3(12)

#######################################################################
# child class having an extra attribute

class Child4(Parent):

    def __init__(self, value, a, b):
        self.a = a
        self.b = b
        super().__init__(value)     # Parent.__init__(self, value)

    def demo(self):
        print(self.a, self.b, self.value)












