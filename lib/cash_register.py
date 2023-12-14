#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price
            self.last_transaction_amount = price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items[-1]
            last_item_quantity = self.items.count(last_item)
            
            self.total -= last_item_quantity * self.last_transaction_amount
            self.items = self.items[:-last_item_quantity]

            if not self.items:
                self.total = 0.0
        else:
            print("No transactions to void.")








