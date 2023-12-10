class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def use(self):
        print(f"I'm currently using an {self.model} by {self.brand} which i bought for {self.price}")

my_smartphone = Smartphone("Apple", "iPhone 12 Pro Max", "120000")
my_smartphone.use()