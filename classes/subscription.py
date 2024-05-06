import json
class Subscription:
    '''
    Attributes:
        subscription_name: str
        cost: float
        one_time_payment: float
        pay_period: str
    '''
    def __init__(self):
        '''Creates the subscription object'''
        self.subscription_name = ' ' 
        self.cost = 0
        self.one_time_payment= 0
        self.pay_period = ''
        
    def __str__(self) -> str:
        return "Subscription: " + self.subscription_name +"\nCost: "+ str(self.cost) + "\nOne time payment: "+ str(self.one_time_payment) + "\nPay period: " + self.pay_period
    
    
    def to_json(self):
        return json.dumps(self.__dict__)

    
    def set_subscription(self, subscription_name: str):
        '''Creates and sets the attributes of the subscription object'''
        while True:
            
            if not subscription_name:
                subscription_name = input("Please enter a valid subscription name: ")
                
            else:
                self.subscription_name = subscription_name
                break
            # try:
            #     if not subscription_name:
            #         raise ValueError("Please enter a valid subscription name")
            # except (TypeError, ValueError) as e:
            #     print("Error:", e)
            #     subscription_name = input("Please enter a valid subscription name: ")
            # else:
            #     self.subscription_name = subscription_name
            #     break
            
        # self.subscription_name = subscription_name
        '''Now we have to get the cost of the subscription and checkk it is a valid input'''
        valid = False
        while valid != True:
            try:
                self.cost = float(input("\nWhat is the monthly cost of this subscription: "))
                if self.cost <= 0:
                    raise ValueError
            except ValueError:
                print("The value must be an integer greater than 0")
            else:
                valid = True
        return self.subscription_name, self.cost
            

    def set_pay_period(self,pay_period: str):
        '''Setting and validating the pay period'''
       #checking validity of the information inputted 
        while True:
            try:
                year = int(pay_period[:4])
                month = int(pay_period[5:7])
                day = int(pay_period[8:10])
                
                if year < 1960 or year > 2024:
                    raise ValueError("Invalid year. Please enter a year between 1960 and 2024.")
                if month < 1 or month > 12:
                    raise ValueError("Invalid month. Please enter a month between 1 and 12.")
                if day < 1 or day > 31:
                    raise ValueError("Invalid day. Please enter a day between 1 and 31.")
            except (ValueError, IndexError) as e:
                print("Error:", e)
                pay_period = input("Enter a valid expense date (YYYY-MM-DD): ")
            else:
                self.pay_period = f"{year:04d}-{month:02d}-{day:02d}"
                return self.pay_period
                
    def set_one_time_payment(self, one_time_payment:float):
        '''sets the one time payment for the subscription Object'''
        valid = False
        while valid != True:
            try:
                if float(one_time_payment) <= 0:
                    raise ValueError
                
            except ValueError:
                one_time_payment = input("Enter a valid payment value   ")
            else:
                valid = True
                self.one_time_payment = one_time_payment
                
        return self.one_time_payment
    
    @staticmethod
    def from_json(json_string):
        '''Creates a static instance based on given json string
            following format of to_json() method's json string
        '''
        attr_dict = json.loads(json_string)
        
        obj = Subscription()
        
        obj.subscription_name = attr_dict["Subscription Name"]
        obj.cost = attr_dict["Subscription Cost"]
        obj.one_time_payment = attr_dict["One time payment"]
        obj.pay_period = ["Pay Period"]
        
        return obj
        
    @staticmethod
    def create():
        '''Static method of the class used to create an instance of the class while prompting the user'''
        sub = Subscription()
        name = input("\nEnter the name of your subscription: ")
        sub.set_subscription(name)
        date = input("\nEnter the expense date (YYYY-MM-DD): ")
        sub.set_pay_period(date)
        payment = input("\nEnter the one time payment ")
        sub.set_one_time_payment(payment)
        return sub
        
        
        

def main():
    #Create a subscription object
    sub = Subscription.create()
    
    # #Menu
    # while True:
    #     print("\nSelect one")
    #     print("1. Add a subscription    ")
    #     print("2. Set pay period    ")
    #     print("3. Make a one time payment   ")
    #     print("4. View subscription details ")
    #     print("5. Exit  ")
        
    #     choice = input("\nChoose an option(1-5):    ")
    #     print(choice)
        
    #     if choice == "1":
    #         #Adding a subscription
    #         name = input("\nEnter the name of the subscritpion: ")
    #         sub.set_subscription(name)
    #     elif choice == "2":
    #         # Set subscription date
    #         date = input("\nEnter the expense date (YYYY-MM-DD): ")
    #         sub.set_pay_period(date)
            
    #     elif choice == "3":
    #         #sets the one time payment for the subscription
    #         payment = input("Enter the one time payment ")
    #         sub.set_one_time_payment(payment)
            
    #     elif choice == "4" : 
    #         if sub.cost == 0:
    #             print("Please fill out subscription details first")
    #             continue
                
    #         # Showing all the details of said subscription
    #         print("\nSubscription Details: ")
    #         print(f"Subscription Name: {sub.subscription_name}")
    #         print(f"Cost: ${sub.cost:.2f}")
    #         print(f"Subscription Date: {sub.pay_period}")
    #         print(f"One Time Payment: ${sub.one_time_payment}")
            
    #     elif choice == "5":
    #         #Exiting the program
    #         print("\n Exiting the program. ")
    #         break
    #     else:
    #         print("\nInvalid choice please try again")
            
    json_string = sub.to_json()
    print(json_string)
    print("\n")
    print(sub)
            
if __name__ == "__main__":
    main()