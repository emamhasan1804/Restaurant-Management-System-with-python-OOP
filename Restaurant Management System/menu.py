class Menu:
    def __init__(self):
        self.items = []
    def addItem(self,item):
        self.items.append(item)
    def findItem(self,itemName):
        for item in self.items:
            if item.name.lower() == itemName.lower():
                return item
        return None
    def removeItem(self,itemName):
        item = self.findItem(itemName)
        if item:
            self.items.remove(item)
            print("Item removed from menu")
        else:
            print("Item not found on the menu")

    def showMenu(self):
        print("*******Menu*******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
