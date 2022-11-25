# creating a menu for restaurant order 
class Menu:
    def __init__(self,food,drink,Quatity):
        self.food = ["1.Rice and Meat: 6000","2.Rice and Fish: 15000","3.Rice and Chicken: 10000","4.Potato and Meat: 5000","5.Potato and Fish: 10000","6.Potato and Chicken: 8000","7.Beans and Meat: 4000","8.Beans and Fish: 8000","9.Beans and Chicken: 6000"]
        self.drink = drink
        self.Quatity = Quatity
  
    def display(self):
        print("...................Menu......................")
        print("1.Food \n2.Drink")
        Choice=int(input("Enter your choice:"))
        
        # Checking the choice
        if Choice ==1:
            print(".............Food..............")
            for i in self.food:
                print(i)
            
            FoodChoice=int(input("Enter your  Food choice:"))
            if FoodChoice == 1:
                print("You have selected :Rice and Meat")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*6000
                print("Bill: ",Bill)
            elif FoodChoice == 2:
                print("You have selected :Rice and Fish")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*15000
                print("Bill: ",Bill)
                
            elif FoodChoice == 3:
                print("You have selected :Rice and Chicken")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*10000
                print("Bill: ",Bill)
                
            elif FoodChoice == 4:
                print("You have selected :Potato and Meat")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*5000
                print("Bill: ",Bill)
                
            elif FoodChoice == 5:
                print("You have selected :Potato and Fish")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*10000
                print("Bill: ",Bill)
            elif FoodChoice == 6:
                print("You have selected :Potato and Chicken")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*8000
                print("Bill: ",Bill)
            elif FoodChoice == 7:
                print("You have selected :Beans and Meat")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*4000
                print("Bill: ",Bill)
            elif FoodChoice == 8:
                print("You have selected :Beans and Fish")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*8000
                print("Bill: ",Bill)
                
            elif FoodChoice == 9:
                print("You have selected :Beans and Chicken")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*6000
                print("Bill: ",Bill)
                
            else:
                print("Invalid Choice")
        
        elif Choice == 2:
            print(".............Drink..............")
            for i in self.drink:
                print(i)
            DrinkChoice=int(input("Enter your  Drink choice:"))
            if DrinkChoice == 1:
                print("You have selected :Coca Cola")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*1000
                print("Bill: ",Bill)
            elif DrinkChoice == 2:
                print("You have selected :Fanta")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*1000
                print("Bill: ",Bill)
            elif DrinkChoice == 3:
                print("You have selected :Sprite")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*1000
                print("Bill: ",Bill)
            elif DrinkChoice == 4:
                print("You have selected :Pepsi")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*1000
                print("Bill: ",Bill)
            elif DrinkChoice == 5:
                print("You have selected :Water")
                self.Quatity=int(input("Enter the quantity:"))
                Bill=self.Quatity*500
                print("Bill: ",Bill)
            else:
                print("Invalid Choice")
                
        else:
            print("Invalid Choice")
             
             
def main():
    food = ["1.Rice and Meat: 6000","2.Rice and Fish: 15000","3.Rice and Chicken: 10000","4.Potato and Meat: 5000","5.Potato and Fish: 10000","6.Potato and Chicken: 8000","7.Beans and Meat: 4000","8.Beans and Fish: 8000","9.Beans and Chicken: 6000"]
    drink = ["1.Coke: 1000","2.Fanta: 1000","3.Sprite: 1000","4.Juice: 1000","5.Water: 1000"]
    Quatity = 0
    menu = Menu(food,drink,Quatity)
    menu.display()
    
main()   
