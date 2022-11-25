
# from Menu1 import *
# # Making payment basing on the Summation of the Order from the Table method
# class Payment(Customer):
#         def __init__(self):
#             self.total = 0
#             self.discount = 0
#             self.amount = 0
#             self.pay = 0
#             self.change = 0
#             self.customer = Customer()
            
#         def pay(self):
#             print("Welcome to the payment section")
#             # Option to pay with cash or card
#             print(tabulate([['1', 'Cash'], ['2', 'Card']], headers=['S/N', 'Payment Method']))
            
#             if self.pay == 1:
#                 self.total = self.customer.Amount()
#                 print("Your total amount is : ",self.total)
#                 self.pay = int(input("Enter your amount : "))
#                 self.change = self.pay - self.total
#                 print("Your change is : ",self.change)
                
#             elif self.pay == 2:
#                 self.total = self.customer.Amount()
#                 print("Your total amount is : ",self.total)
#                 self.pay = int(input("Enter your amount : "))
#                 self.change = self.pay - self.total
#                 print("Your change is : ",self.change)
                
#             else:
#                 print("Invalid option")
#                 self.pay()
            
            
        