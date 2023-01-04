""
"""
Multi level inheritance
* It is a type of inheritance where a Child1 class(sub class) will be deriving
  properties of Parent class and one more child class say Child2 will be 
  deriving from the Child2 class.
  
            Parent
               ^
               |
               |
            Child1
               ^
               |
               |
            Child2
"""


class A:
    def demo(self):
        print("Class A demo")


class B(A):
    def demo(self):
        print("class B demo")
        super().demo()


class C(B):
    def demo(self):
        print("class C demo")
        super().demo()


c = C()
print(C.__mro__)
# <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

