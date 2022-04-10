class ShoppingCart:
    # class variables
    products = {"iPhone": 5, "iWatch": 2, "iMac": 3, "iPad": 4}
    prices = {"iPhone": 800, "iWatch": 2500, "iMac": 2500, "iPad": 3500}

    # Constructor/ initializer
    def __init__(self):
        self.cart = []

    # Instance methods
    def add_item(self, name, quantity):
        if name in self.__class__.products:     # ShoppingCart.products
            if quantity <= self.__class__.products[name]:
                self.cart.append({"name": name, "quantity": quantity, "price": self.__class__.prices[name]})
                self.__class__.products[name] -= quantity
            else:
                raise Exception(f"Out of Stock")
        else:
            raise Exception("Invalid Product")

    def total_cost(self):
        total = 0.0
        return sum([item["quantity"] * item["price"] for item in self.cart])

    def remove_item(self, name):
        for item in self.cart:
            if item["name"] == name:
                if item["quantity"] == 1:
                    self.cart.remove(item)
                else:
                    item["quantity"] = item["quantity"] - 1


c1 = ShoppingCart()
c2 = ShoppingCart()
print(c1.__dict__)
print(c2.__dict__)
