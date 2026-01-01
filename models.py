class Receipt:
    def __init__(self, id, store, total_amount, date, payer, items):
        self.id = id
        self.store = store 
        self.total_amount = total_amount
        self.date = date
        self.payer = payer 
        self.items = items 
        
class Store:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Split:
    def __init__(self, id, receipt_id, item_id, payer_id, debtor_id, amountOwed, amountPaid):
        self.id = id
        self.receipt_id = receipt_id
        self.item_id = item_id
        self.payer_id = payer_id
        self.debtor_id = debtor_id
        self.amountOwed = amountOwed
        self.amountPaid = amountPaid