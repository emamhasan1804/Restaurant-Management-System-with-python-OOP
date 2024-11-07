from food_item import FoodItem
from menu import Menu
from order import Order
from restaurant import Restaurant
from user import User,Employee,Admin,Customer
sultans_dine = Restaurant('Sultans Dine')
def customerMenu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    
    customer = Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f"\nWelcome {customer.name}")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        option = int(input("Enter your choice : "))

        if option == 1:
            customer.showMenu(sultans_dine)
        elif option == 2:
            item_name = input("Enter item name : ")
            quantity = int(input("Enter item quantity : "))
            customer.addToCart(sultans_dine,item_name,quantity)
        elif option == 3:
            customer.viewCart()
        elif option == 4:
            customer.payBill()
        elif option == 5:
            break
        else:
            print("Invalid Input")


def adminMenu():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    admin = Admin(name,phone,email,address)
    # admin = Admin(name,phone=phone,email=email,address=address)

    while True:
        print(f"\nWelcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Remove Items")
        print("6. Exit")

        option = int(input("Enter your choice : "))

        if option == 1:
            item_name = input("Enter Item name : ")
            item_prince = int(input("Enter item price : "))
            quantity = int(input("Enter item quantity : "))
            admin.addItem(sultans_dine,FoodItem(item_name,item_prince,quantity))
        elif option == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            desig = input("Enter employee designation : ")
            age = int(input("Enter employee age : "))
            salary = int(input("Enter employee salary : "))
            address = input("Enter employee address : ")
            admin.addEmployee(sultans_dine,Employee(name,phone,email,address,age,desig,salary))
        elif option == 3:
            admin.viewEmployee(sultans_dine)
        elif option == 4:
            admin.viewMenu(sultans_dine)
        elif option == 5:
            name = input("Enter item name : ")
            admin.removeItem(sultans_dine,name)
        elif option == 6:
            break
        else:
            print("Invalid Input")

while True:
    print("\n\t\t Welcome \n")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    option = int(input("Enter your option : "))

    if option == 1:
        adminMenu()
    elif option == 2:
        customerMenu()
    elif option == 3:
        break
    else:
        print("Invalid Input")