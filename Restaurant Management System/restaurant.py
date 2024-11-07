from menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    def addEmployee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} is joind as a {employee.designation}")
    def viewEmployee(self):
        print("Employee List : ")
        for emp in self.employees:
            print(f"Name : {emp.name} , phone : {emp.phone} , email : {emp.email} , address : {emp.address}")
