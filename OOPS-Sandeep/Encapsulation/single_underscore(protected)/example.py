class Account:
    _interest = 0.04        # internal purpose only

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # not supposed to call this method directly
    def _spam(self):
        print("Account _spam")

    def demo(self):
        self._spam()    # internally using _spam as it cannot be accessed outside
        print("Account demo")

# we can access _interest and _spam() outside the class but it should not be done
# according to python convention

#########################################################################
# without checking these internal attributes, we might pass bad data to it and
# get wrong answer so setters should be created for validating
class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def mul(self):
        return self._a * self._b

##########################################################################


