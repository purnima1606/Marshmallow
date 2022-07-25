""
"""
Hybrid inheritance - It is a type of inheritance where 2 or more inheritance will be combined in the
inheritance hierarchy
"""

# Hierarchical inheritance
class Parent:
    def spam(self):
        print("Parent spam")


class Child1(Parent):
    def spam(self):
        print("Child1 spam")
        super().spam()


class Child2(Parent):
    def spam(self):
        print("Child2 spam")
        super().spam()


# Multiple inheritance
class Child3(Child1, Child2):
    pass

c = Child3()
print(Child3.__mro__)
c.spam()

"""
(<class '__main__.Child3'>, <class '__main__.Child1'>, <class '__main__.Child2'>, <class '__main__.Parent'>, <class 'object'>)
Child1 spam
Child2 spam
Parent spam
"""

"""
While looking up for spam() from child3 in multiple inheritance,
 * Child3 will be searched first and then Child1 class will be searched
 * But super() in Child2 will not call the parent class of Child1, but it 
   will consider the next class in mro(i.e., Child2) as super() class 
 * Child2 will be checked for presence of spam() if it not present then
   finally from Child2 it will go to Parent class.
"""
