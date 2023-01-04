# Hierarchical inheritance example

class BankAccount:
    interest_rate = 0.04

    def __init__(self, fname, lname, balance):
        self.fname = fname
        self.lname = lname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise Exception("Insufficient balance")

    def roi(self):
        interest_amount = self.balance * self.__class__.interest_rate  # Accessing class variable via classname
        self.balance = self.balance + interest_amount


class SBAccount(BankAccount):       # Single level inheritance
    interest_rate = 0.05

    # partial overriding of withdraw method
    def withdraw(self, amount):
        if amount > 5000:
            raise Exception("Maximum withdraw limit exceeded")
        super().withdraw(amount)        # partial overriding or method chaining


class SalaryAccount(BankAccount):
    MAX_DRAFT_AMOUNT = 10000

    def __init__(self, fname, lname, balance=0):
        self.is_first_month_salary = True
        self.draft_amount_taken = 0
        super().__init__(fname, lname, balance)     # constructor chaining

    # partial overriding of withdraw method
    def deposit(self, amount):
        if self.is_first_month_salary:
            self.is_first_month_salary = False  # once the first month salary is taken from next it should be false
            super().deposit(amount + 1000)
        else:
            super().deposit(amount)

    def overdraft(self, amount):
        if self.draft_amount_taken + amount <= self.__class__.MAX_DRAFT_AMOUNT:
            super().deposit(amount)
            self.draft_amount_taken += amount
        else:
            raise Exception("Maximum overdraft amount exceeded")


class SeniorCitizenAccount(BankAccount):      # Multi level inheritance
    interest_rate = 0.06

    # partial overriding of withdraw method
    def withdraw(self, amount):
        if amount > 10000:
            raise Exception("Maximum withdraw limit exceeded")
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 0.095

    # completely overriding "withdraw" method of "BankAccount" (Parent class)
    def withdraw(self, amount):
        raise Exception("Cannot withdraw amount")

    # partial overriding
    def deposit(self, amount):
        if amount < 1000:
            raise Exception("Minimum deposit amount is 1000")
        super().deposit(amount)


e1 = SalaryAccount("steve", "jobs")
e2 = SalaryAccount("Bill", "Gates")
c1 = SeniorCitizenAccount("Bill", "Gates", 100000)
c2 = SukanyaSamrudhiAccount("Sudha", "Murthy", 100000)



