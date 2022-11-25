from Menu1 import *
from RestaurantDatabases.payment import *
from Customer import *
from getpass import getpass
class Dashboard:
    def __init__(self,username,password):
        self._username="customer"
        self._password = "customer"
    
    def options (self):
        #  Designing the admin menu
        print("*"*120)
        print("Welcome to fast food restaurant")   
        print("*"*120)   
        
    #    Using Tabulate to display the menu with Customer Login
        print(tabulate([['1', 'Customer Login'], ['2', 'Admin Login'],['3','Help']], headers=['S/N', 'Options']))
       
        option=int(input("Enter your Option:"))
        # Customer Options
        if option == 1:
            
            print("Customer Login")
            self.username = input("Enter username: \n") 
            # Using the getpass module to get the password
            self.password = getpass("Enter password: \n")
            if self.username == "Customer" and self.password == "Customer":
                # print("Welcome to our restaurant")
                print("Welcome our esteemed customer")
                customer = Customer()
                customer.Welcome()              
            else:
                print("Invalid username or password")
                self.options()
                
        # Admin options
        elif option ==2:
            print("Admin Login")
            self._username = input("Enter username: \n")
            self._password = getpass("Enter password: \n")
            
            if self._username == "Admin" and self._password == "Admin":
                print("Welcome Admin")
                admin = Employee()
                admin.options()
            else:
                print("Invalid username or password")
                self.options()
        elif option == 3:
            print("...Welcome to the help section...")
            print("...Please contact the admin for help...")
            # Displaying the customer help information
            # use the tabulate module to display the help information the restaurant contact details
            print(tabulate([['Name', 'Phone Number', 'Email'], ['Admin', '08123456789', 'fastfoods@gmail.com']], headers=['Name', 'Phone Number', 'Email']))
            
            # Ask user if the information is helpful
            print("Was the information helpful?")
            print(tabulate([['1', 'Yes'], ['2', 'No']], headers=['S/N', 'Choice']))
            if int(input("Enter your choice : ")) == 1:
                print("Thank you for your feedback")
                # Ask user if they want to continue using the system
                print("Do you want to continue using the system?")
                print(tabulate([['1', 'Yes'], ['2', 'No']], headers=['S/N', 'Choice']))
                if int(input("Enter your choice : ")) == 1:
                    self.options()
                    
                else:
                    print("Thank you for using our system")
                    exit()
                    
            else:
                print("Thank you for your feedback")
                # Ask user if they want to continue using the system
                print("Do you want to continue using the system?")
                print(tabulate([['1', 'Yes'], ['2', 'No']], headers=['S/N', 'Choice']))
                if int(input("Enter your choice : ")) == 1:
                    self.options()
                    
                else:
                    print("Thank you for using our system")
                    exit()
            
            