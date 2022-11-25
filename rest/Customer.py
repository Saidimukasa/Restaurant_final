from Menu1 import *
class Customer(Drinks,Food):
    def __init__(self):
        self.drink = Drinks()
        self.food = Food()
        self.take = 0
        self.apply = 0
        self.Name = " "
        self.tableNumber = 0
    def setName(self,CustomerName):
        self.Name = CustomerName
    def getName(self):
        return self.Name
    def setTable(self,tablenumber):
        self.tableNumber = tablenumber
    def getTable(self):
        return self.tableNumber
        
    # This method is used to get the choice of the customer  
    def choice(self):
        print("Select the type of service you want")
        # Using tabulate to display the menu
        print(tabulate([['1', 'Food'], ['2', 'Drinks']], headers=['S/N', 'Service']))
        self.take = int(input())
        # This is used to check if the customer wants to order food or drink
        if self.take == 1:
            print(self.food.Menu())
            self.apply = int(input("Enter your choice : "))
            self.food.choice(self.apply)
            
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more food?,or get a drink (y/n) : ")
            if next == 'y':
                self.choice()
        # This is used to check if the customer wants to order drink  
        elif self.take == 2:
            # This is used to display the menu of the drinks
            print(self.drink.Menu())
            # This is used to get the choice of the customer
            self.apply = int(input("Enter your choice : "))
            self.drink.choice(self.apply)
            
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more drinks?,or get food (y/n) : ")
            if next == 'y':
                self.choice()
        # This method is used to return the Total amount of the customer request
    def Amount(self):
        final =  self.food.getTotal() + self.drink.getTotal()
        return final
    
    
    #This method is used to get the number of people on a table
    def Tables(self):
        RestaurantCustomer=[]
        # This is used to get the number of people on a table
        # Enabling the User to enter their name and Store it in a list
        customername= input("Order Customer's Name: ")
        self.setName(customername)
        RestaurantCustomer.append(customername)
        # This is used to check if the table is available
        # Show Available tables
        print("Available tables are: ")
        print(tabulate([['1', 'Available'], ['2', 'Available'], ['3', 'Available'], ['4', 'Available'], ['5', 'Available'], ['6', 'Available'], ['7', 'Available'], ['8', 'Available'], ['9', 'Available'], ['10', 'Available']], headers=['Table Number', 'Status']))
        TableNumber= int(input("Enter the table number : "))
        # Storing the Taken table in a list
        self.setTable(TableNumber)
        Tables=[1,2,3,4,5,6,7,8,9,10]
        while True:
            if TableNumber in Tables:
                Tables.remove(TableNumber)
                print("Table is available")
                break
            else:
                print("Table is not available")
                TableNumber= int(input("Enter the table number : "))

             #validate if table is booked or not   


    # Payment Method 
    def Payment(self,finalAmount):
        print(f"TotalAmount: {finalAmount}")
        print("Welcome to the payment section")
        print(tabulate([['1', 'Cash'], ['2', 'Card']], headers=['S/N', 'Payment Method']))
        payment = int(input("Enter your choice : "))
        
        if payment == 1:
            print("Cash Payment")
            amount= int(input("Enter the amount : "))
            if amount >= finalAmount:
                    print("Your change is ",amount - finalAmount)
            else:
                print("Insufficient amount")
                Balance= finalAmount - amount
                print("Your balance is ",Balance)
            
        elif payment == 2:
            print("Card Payment")
            amount= int(input("Enter the amount : "))
            if amount >= finalAmount:
                    print("Your change is ",amount - finalAmount)
                    
            else:
                print("Insufficient amount")
                Balance= finalAmount - amount
                print("Your balance is ",Balance)
                
                
            # Welcome Method 
    def Welcome(self):
        summationz = 0
        storage = []
        self.Tables()
        number = int(input("Enter the number of people on the table : "))
        for i in range(number):
            print("Customer ",i+1)
            self.choice()
            
            storage.append(self.Amount())
            length = len(storage)
            for i in range(length):
                summationz += storage[i]
            print("*"*50)
        print(f"OrderCustomerName:{self.getName()}\nTableNumber:{self.getTable()}\n")
        print("*"*50)
        self.Payment(summationz)
        self.Receipt()
        
    # Ask user if they want to print receipt

    def Receipt(self):
        # Ask user if they want to print receipt
        print("Do you want to print receipt?")
        print(tabulate([['1', 'Yes'], ['2', 'No']], headers=['S/N', 'Choice']))
        
        
        if int(input("Enter your choice : ")) == 1:
        #    Using the tabulate module to display the receipt
            
            print("."*50)
            print(".......Receipt.........")
            print(tabulate([['OrderCustomerName', self.getName()], ['TableNumber', self.getTable()], ['TotalAmount', self.Amount()]], headers=['Data', 'Details']))
            print("."*50)   
        
                 
class Employee(object):
    
    def options(self):
        #using a dictionary to store the options
        AdminOptions = {1:'View Food Menu',2:'View Drinks Menu',3:'View Customer Orders',4:'View Customer Bill',5:'Logout'}
        # Displaying the options from the dictionary
        for key,value in AdminOptions.items():
            print(key,value)
            
        # Getting the choice of the Admin
        Choice= int(input("Enter your choice : "))
        if Choice == 1:
                self.viewfood()
                
        elif Choice == 2:
                self.viewDrinks()
                
        elif Choice == 3:
                self.viewCustomerOrders()
                
        elif Choice == 4:
                self.viewCustomerBill()
                
        elif Choice == 5:
                print("You have successfully logged out")
                exit()
                
                
    def viewfood(self):
        print("Food Menu")
        #using tabulate to display the menu
        print(tabulate([['1', 'Rice and Meat', '6000'], ['2', 'Rice and Fish', '15000'], ['3', 'Rice and Chicken', '10000'], ['4', 'Potato and Meat', '5000'], ['5', 'Potato and Fish', '10000'], ['6', 'Potato and Chicken', '8000'], ['7', 'Beans and Meat', '4000'], ['8', 'Beans and Fish', '8000'], ['9', 'Beans and Chicken', '6000']], headers=['S/N', 'Food', 'Price']))
        #  Ask user if they want to go back to the main menu
        back= input("Do you want to go back to the main menu (y/n) : ")
        if back == 'y':
            self.options()
        else:
            exit()
        
    def viewDrinks(self):
        print("Drinks Menu")
        #using tabulate to display the menu
        print(tabulate([['1', 'Coca Cola', '1000'], ['2', 'Fanta', '1000'], ['3', 'Sprite', '1000'], ['4', 'Pepsi', '1000'], ['5', 'Water', '1000'], ['6', 'Milk', '1000'], ['7', 'Ice Cream', '1000'], ['8', 'Cake', '1000'], ['9', 'Bread', '1000']], headers=['S/N', 'Drinks', 'Price']))
        back= input("Do you want to go back to the main menu (y/n) : ")
        if back == 'y':
            self.options()
        else:
            exit()
        
    def viewCustomerOrders(self):
        print("Customer Orders")
        #using tabulate to display the menu
        print(tabulate([['1', 'Rice and Meat', '6000'], ['2', 'Rice and Fish', '15000'], ['3', 'Rice and Chicken', '10000'], ['4', 'Potato and Meat', '5000'], ['5', 'Potato and Fish', '10000'], ['6', 'Potato and Chicken', '8000'], ['7', 'Beans and Meat', '4000'], ['8', 'Beans and Fish', '8000'], ['9', 'Beans and Chicken', '6000']], headers=['S/N', 'Food', 'Price']))
        # Viewing Customer Orders
        print("Customer Orders")
        
    def viewCustomerBill(self):
        # Basing the bill on the food and drinks ordered
        print("Customer Bill")
        
    def Logout(self):
        print("You have successfully logged out")
        exit()
       
        
                 
        
        
           
     

        
           
