# overriding parent class variable in Child class


class Spam:
    a = 10

    def apple(self):
        print(f"Apple {self.__class__.a}")

"""
* using self.__class__.a will take the address of the invoking object's class
  and not the class in which it is present.
* If will use Spam.a instead of self.__class__.a, no matter whichever object 
  might be calling that variable, it will always get spam class' variable a
"""


class Demo(Spam):
    a = 20

    def google(self):
        print("google")


d = Demo()
print(d.a)  # 20

# instead of self.__class__.a if we use Spam.a, then the output will be 10

