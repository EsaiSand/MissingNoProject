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
    def set_subscription(self, subscription_name: str):
        '''Creates and sets the attributes of the subscription object'''
        while True:
            try:
                if not subscription_name.isalpha():
                    raise ValueError("The subscription name must contain only letters")
            except (TypeError, ValueError) as e:
                print("Error:", e)
                subscription_name = input("Please enter a valid subscription name: ")
            else:
                self.subscription_name = subscription_name
                break
            
        self.subscription_name = subscription_name
        '''Now we have to get the cost of the subscription and checkk it is a valid input'''
        valid = False
        while valid != True:
            try:
                self.cost = float(input("What is the monthly cost of this subscription: "))
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



def main():
    #Create a subscription object
    sub = Subscription()
    
    #Menu
    while True:
        print("\nSelect one")
        print("1. Add a subscription    ")
        print("2. Set pay period    ")
        print("3. Make a one time payment   ")
        print("4. View subscription details ")
        print("5. Exit  ")
        
        choice = input("\nChoose an option(1-5):    ")
        print(choice)
        
        if choice == "1":
            #Adding a subscription
            name = input("\nEnter the name of the subscritpion: ")
            sub.set_subscription(name)
        elif choice == "2":
            # Set subscription date
            date = input("\nEnter the expense date (YYYY-MM-DD): ")
            sub.set_pay_period(date)
            
        elif choice == "3":
            #sets the one time payment for the subscription
            payment = input("Enter the one time payment ")
            sub.set_one_time_payment(payment)
            
        elif choice == "4" : 
            if sub.cost == 0:
                print("Please fill out subscription details first")
                continue
                
            # Showing all the details of said subscription
            print("\nSubscription Details: ")
            print(f"Subscription Name: {sub.subscription_name}")
            print(f"Cost: ${sub.cost:.2f}")
            print(f"Subscription Date: {sub.pay_period}")
            print(f"One Time Payment: ${sub.one_time_payment}")
            
        elif choice == "5":
            #Exiting the program
            print("\n Exiting the program. ")
            break
        else:
            print("\nInvalid choice please try again")
if __name__ == "__main__":
    main()