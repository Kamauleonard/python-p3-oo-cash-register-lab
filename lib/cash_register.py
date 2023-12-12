class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.last_transaction_amount = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price
            self.last_transaction_amount = price

    def apply_discount(self):
        if self.discount > 0:
            discount_factor = 1 - (self.discount / 100.0)
            self.total *= discount_factor
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.last_transaction_amount
            self.total -= last_item_price
            self.items.pop()
            self.last_transaction_amount = 0
            if not self.items:
                self.total = 0.0
        else:
            print("No transactions to void.")
    
    def get_total(self):
        return self.total
