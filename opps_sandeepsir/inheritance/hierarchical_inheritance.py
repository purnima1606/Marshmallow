""
"""
Hierarchical inheritance
* It is a type of inheritance in which a single base/parent class will be 
  derived/inherited by more than one child classes.
                            
                                Parent
                                   |
                            |             |
                        Child1          Child2
"""

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


c = Child1()
print(Child1.__mro__)
c.spam()
""" 
o/p:  
(<class '__main__.Child1'>, <class '__main__.Parent'>, <class 'object'>)
Child1 spam
Parent spam
"""

c = Child2()
print(Child2.__mro__)
c.spam()
""" 
o/p:  
(<class '__main__.Child2'>, <class '__main__.Parent'>, <class 'object'>)
Child2 spam
Parent spam
"""

