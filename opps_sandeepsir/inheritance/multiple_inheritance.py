""
"""
*********************** Multiple Inheritance **************************
1. Inheriting properties of multiple parent classes into single parent class
2. If all the parents has same method and the child is inheriting from both,
then the chaining should be done with the help of parent class name
    i.e., ParentClass.method_name(self, parameters)
3. If super() function is used for chaining then the immediate parent class
or the parent class written first for inheriting will be considered.
4. Order of inheritance will always be from left to right.
5. MRO(method resolution order) - It is an order in which python looks up for 
an attribute in an inheritance hierarchy
    - MRO in multiple inheritance will always be from right to left
    
                Parent1             Parent2
                    |                   |
                               |
                            Child
    
"""
# only one parent class having constructor
class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print(f"Executing Parent Apple {self.value}")

    def google(self):
        print(f"Executing Parent Google")
        self.apple()


class Parent2:
    def facebook(self):
        print("Executing Parent2 Facebook")


# chaining constructor in Child5
class Child5(Parent, Parent2):

    def __init__(self, value):
        super().__init__(value)     # Parent.__init__(self, value)

#############################################################################
# Both the parent classes having constructor

class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print(f"Executing Parent Apple {self.value}")

    def google(self):
        print(f"Executing Parent Google")
        self.apple()


class Parent2:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def facebook(self):
        print("Executing Parent2 Facebook")


# It is the responsibility of child6 to initialize all the attributes of
# both the parent classes
class Child6(Parent, Parent2):

    def __init__(self, value, fname, lname, age):
        Parent.__init__(self, value)
        Parent2.__init__(self, fname, lname, age)


c = Child6(32, "steve", "jobs", 24)
print(Child6.__mro__)
# (<class '__main__.Child6'>, <class '__main__.Parent'>, <class '__main__.Parent2'>, <class 'object'>)
##########################################################################









