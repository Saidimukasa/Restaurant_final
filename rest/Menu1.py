from abc import ABC, abstractmethod
from tabulate import tabulate

# Creating a class for the Restaurant services
class Services(ABC):
    def __init__(self,):
        self
    # abstract method Choice
    @abstractmethod
    def choice (self):
        pass
    # abstract method Amount
    @abstractmethod
    def setTotal(self):
        pass
    # abstract method GetTotal
    @abstractmethod
    def getTotal(self):
        pass

# Food class and this class inherits from the Services class  
class Food(Services):
    
    def __init__(self):
        super().__init__()
        self.total = 0    
    # This method is used to get the choice of the customer
    def choice(self,take):
        self.availability = {1: {'name': 'Rice and Meat', 'price': 6000}, 2: {'name': 'Rice and Fish', 'price': 15000}, 3: {'name': 'Rice and Chicken', 'price': 10000}, 4: {'name': 'Potato and Meat', 'price': 5000}, 5: {'name': 'Potato and Fish', 'price': 10000}, 6: {'name': 'Potato and Chicken', 'price': 8000}, 7: {'name': 'Beans and Meat', 'price': 4000}, 8: {'name': 'Beans and Fish', 'price': 8000}, 9: {'name': 'Beans and Chicken', 'price': 6000}}
        if take in self.availability:
            print("You have selected: ",self.availability[take]['name'])
            self.quantity = int(input("Enter the quantity:"))
            self.bill = self.availability[take]['price'] * self.quantity
            self.setTotal(self.bill)
            print("Bill: ",self.getTotal())
            
    # This method is used to Display the menu of the restaurant to the customer
    def Menu(self):
        # Using tabulate to display the menu
         print(tabulate([['1', 'Rice and Meat', '6000'], ['2', 'Rice and Fish', '15000'], ['3', 'Rice and Chicken', '10000'], ['4', 'Potato and Meat', '5000'], ['5', 'Potato and Fish', '10000'], ['6', 'Potato and Chicken', '8000'], ['7', 'Beans and Meat', '4000'], ['8', 'Beans and Fish', '8000'], ['9', 'Beans and Chicken', '6000']], headers=['S/N', 'Food', 'Price']))
    # This method is used to set the total amount of the customer
    
    def setTotal(self,bill):
        self.total = self.total + bill
        return self.total
    # This method is used to get the total amount of the customer
    def getTotal(self):
        return self.total
 
    # class Drinks and this class inherits from the Services class
class Drinks(Services):
    
    def __init__(self):
        super().__init__()
        self.total = 0
        
    #  This method is used to get Drink choice of the customer
    def choice (self,take):
        #  This is the dictionary of the available drinks
        self.availability = {1:{'name':'Coke','price':1000},2:{'name':'Fanta','price':1000},3:{'name':'Sprite','price':1000},4:{'name':'Juice','price':5000},5:{'name':'Water','price':1000}}
        # This is used to check if the drink is available in the dictionary of the available drinks
        if take in self.availability:
            # This is used to get the name of the drink and the quantity of the drink
            print("You have selected: ",self.availability[take]['name'])
            self.quantity = int(input("Enter the quantity:"))
            self.bill = self.availability[take]['price'] * self.quantity
            self.setTotal(self.bill)
            # This is used to get the total bill of the customer
            print("Bill: ",self.getTotal())
            
    def Menu(self):
        # Using tabulate to display the menu
        print(tabulate([['1', 'Coke', '1000'], ['2', 'Fanta', '1000'], ['3', 'Sprite', '1000'], ['4', 'Juice', '5000'], ['5', 'Water', '1000']], headers=['S/N', 'Drink', 'Price']))
    def setTotal(self,bill):
        self.total = self.total + bill
        return self.total
    def getTotal(self):
        return self.total
    
    
# Customer class and this class inherits from the Drinks and Food class
