class Order:
    def __init__(self):
        self.items = {}
    def addItem(self,item,quantity):
        if item in self.items:
            self.items[item]+=item.quantity
        else:
            self.items[item] = item.quantity
    def removeFromCart(self,item):
        if item in self.items:
            del self.items[item]
    @property # ei function ekhon instance or variable hoye geche
    def totalPrice(self):
        return sum(item.price * quantity for item,quantity in self.items.items()) 
    def clear(self):
        self.items = {}
