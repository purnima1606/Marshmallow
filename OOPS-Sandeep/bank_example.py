class BankAccount:
    interest_rate = 0.04        # class variable

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Amount deposited: {amount}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.transactions.append(f"Amount withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def statement(self):
        for item in self.transactions:
            print(item)
        print("-" * 29)
        print("Total available balance:", self.balance)

    def transfer(self, amount, to_account):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            # to_account takes other object's address/dictionary
            to_account.deposit(amount)  # calls deposit method using calling object
            self.balance -= amount

    def roi(self):
        interest_amount = self.balance * BankAccount.interest_rate  # Accessing class variable via classname
        self.balance = self.balance + interest_amount
        self.transactions.append(f"Interest amount deposited: {interest_amount}")


c1 = BankAccount("Steve", 1000)
c2 = BankAccount("Bill", 2000)
# c1.deposit(500)     # BankAccount.deposit(c1, 500)
# c2.withdraw(500)     # BankAccount.withdraw(c2, 500)
# c1.statement()
# c1.transfer(500, c2)   # c1 calls transfer method in turn c2 calls deposit method
# inside transfer()


# Accessing class variables
# print(c1.__class__.interest_rate)
# print(BankAccount.interest_rate)

