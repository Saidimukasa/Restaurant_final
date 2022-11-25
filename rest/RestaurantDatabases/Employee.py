from tabulate import tabulate
from Menu1 import *
from Admin import *
class Employee:
    def __init__(self):
        pass
    def options(self):
        print("*"*120)
        print("Welcome to fast food restaurant")   
        print("*"*120)   
        
    #    Using Tabulate to display the menu with Customer Login
        print(tabulate([["1. View Menu","2. View Orders","3. Exit"]],headers=["View Menu","View Orders","Exit"],tablefmt="fancy_grid"))
       
        option=int(input("Enter your Option:"))
        
        if option == 1:
            menu = Menu()
            menu.display()
            self.options()
        
        elif option == 2:
            order = Order()
            order.display()
            self.options()
        
        elif option == 3:
            print("Thank you for visiting us")
            exit()
        else:
            print("Invalid Option")
            self.options()