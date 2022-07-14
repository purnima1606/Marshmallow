# It is possible to override _attributes in child class

class Account:
    _interest = 0.04

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def _spam(self):
        print("Account _spam")

    def demo(self):
        self._spam()
        print(f"Account demo {self.__class__._interest}")


class SBAccount(Account):
    _interest = 0.05

    def _spam(self):
        print("SBAccount _spam")

sb = SBAccount("abc", 1000)
sb.demo()   # executes SBAccount _spam and prints 0.05

#########################################################################
