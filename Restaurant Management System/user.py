from abc import ABC
from order import Order
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def showMenu(self,restaurant):
        restaurant.menu.showMenu()

    def addToCart(self,restaurant,itemName,quantity):
        item = restaurant.menu.findItem(itemName)
        if item:
            if item.quantity<quantity:
                print(f"Item quantity exceeded !")
            else:
                temp = item.quantity
                item.quantity = quantity
                self.cart.addItem(item,quantity)
                item.quantity = temp - quantity
                print("Item added")
        else:
            print("Item not found")
    def viewCart(self):
        print("*******Cart*******")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price : {self.cart.totalPrice}")

    def payBill(self):
        print(f'Total {self.cart.totalPrice} paid successfully')
        self.cart.clear()

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def addEmployee(self,restaurant,employee):
        restaurant.addEmployee(employee)
    
    def viewEmployee(self,restaurent):
        restaurent.viewEmployee()

    def addItem(self,restaurent,item):
        restaurent.menu.addItem(item)

    def removeItem(self,restaurent,item):
        restaurent.menu.removeItem(item)

    def viewMenu(self,restaurent):
        restaurent.menu.showMenu()
