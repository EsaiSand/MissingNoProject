import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import helpers as help

class Subscription:
    '''
    Attributes:
        subscription_name(str): Name of subscription
        cost(float): Cost of subscription
        once_yearly_cost(float): Holds cost of additional yearly fee for subscription if applicable
        pay_period(str): Describes the recurrance of subscription (Monthly or Anually)
        last_charge(date): Holds date obj of last time subscription was charged
        last_yearly : Holds date obj of last time annual fee was charged (If applicable)
    '''

    CHARGE_INTS = {
        'Monthly': relativedelta(months=1),
        'Yearly': relativedelta(years=1)
    }

    def __init__(self):
        '''Creates the subscription object'''
        self.subscription_name = ' ' 
        self.cost = 0
        self.once_yearly_cost= 0
        self.pay_period = 'Monthly'
        self.last_charge = dt.today()
        self.last_yearly  = dt.today()
        
    def __str__(self):
        yearly_date = ''
        yearly_cost = self.once_yearly_cost
        if self.once_yearly_cost == 0:
            yearly_date = "N/A"
            yearly_cost = "N/A"
        else: 
            yearly_date = self.last_yearly .strftime(r'%x')

        return f"~|{'Subscription': ^15}|{'Cost': ^12}|{'Annual Fee': ^12}|{'Pay Period': ^15}|{'Last Payment': ^15}|{'Last Annual Fee': ^15}|~\n||{self.subscription_name: ^15}|{self.cost: ^12}|{yearly_cost: ^12}|{self.pay_period: ^15}|{self.last_charge.strftime(r'%x'): ^15}|{yearly_date: ^15}||\n"
    
    def calc_fees_since_last_charge(self):
        total = 0.0
        next_common = self.last_charge + Subscription.CHARGE_INTS[self.pay_period]
        next_yearly = self.last_yearly + relativedelta(years=1)
        while next_common < dt.today():
            if next_yearly < dt.today():
                total += self.once_yearly_cost
                self.last_yearly = next_yearly
                next_yearly += relativedelta(years=1)

            total += self.cost
            self.last_charge = next_common
            next_common += Subscription.CHARGE_INTS[self.pay_period]
        
        return total

    def to_json(self):
        last = self.last_charge
        lasty = self.last_yearly
        attr_dict = {
            'name': self.subscription_name,
            'cost': self.cost,
            'Once Yearly': self.once_yearly_cost,
            'Period': self.pay_period,
            'Last paid': [last.strftime("%Y"), last.strftime("%m"), last.strftime('%d')],
            'Last yearly': [lasty.strftime("%Y"), lasty.strftime("%m"), lasty.strftime('%d')]
        }
        return json.dumps(attr_dict, indent=4)

    
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
                self.once_yearly_cost = one_time_payment
                
        return self.once_yearly_cost
    
    @staticmethod
    def from_json(json_string):
        '''Creates a static instance based on given json string
            following format of to_json() method's json string
        '''
        attr_dict = json.loads(json_string)
        
        obj = Subscription()
        
        obj.subscription_name = attr_dict["name"]
        obj.cost = attr_dict["cost"]
        obj.once_yearly_cost = attr_dict["Once Yearly"]
        obj.pay_period = attr_dict["Period"]
        last = attr_dict["Last paid"]
        obj.last_charge = dt(int(last[0]), int(last[1]), int(last[2]))
        lasty = attr_dict["Last yearly"]
        obj.last_yearly = dt(int(lasty[0]), int(lasty[1]), int(lasty[2]))
        
        return obj
        
    @staticmethod
    def create():
        '''Static method of the class used to create an instance of the class while prompting the user'''
        sub = Subscription() 
        sub.subscription_name = input("Subscription name: ")
        sub.cost = help.validate_input(0.0, "What is the subscription's recurring fee? Ignore additional yearly cost if applicable: $", pos=True)
        sub.last_charge = help.validate_date("When was the subscription last charge? Ignore yearly fee charge if applicable.\n(folow MM-DD-YYYY format): ")
        
        choice = help.validate_input("s", "Does the subscription have an additional annual fee? (y/n): ", valids=['y', 'n'])
        if choice == 'y':
            sub.once_yearly_cost = help.validate_input(0.0, "How much is the annual fee?: $", pos=True)
            sub.last_yearly = help.validate_date("When was the annual fee last charged?: ")

        return sub
    def edit_menu(self):
        menu_string = f"Editing subscriptions {self.name}\n\n1. Change subscription name\n2. Change subscription's recurring fee\n3. Change last subscription cost\n4.  Change suncription additional annual fee\n5. Change the annual fee\n6. Change when the annual was last charged\n7. Back\n Selections: "
        while True:
            choice = help.validate_input(1, menu_string, valids=[1,2,3,4,5,6])
            if choice == 1:
                #Changing the Debt name
                self.name = input("Enter new Subscription name:")
            if choice == 2:
                self.cost = help.validate_input(0.0, "Enter new  subscription's recurring fee: ")
            if choice == 3:
                self.last_charge = help.validate_date(0.0, "Enter new subscription charge date (folow MM-DD-YYYY format):")
            if choice == 4:
                self.once_yearly_cost =  help.validate_input("0.0", "Enter new  annual fee:$")
            if choice == 5:
                self.last_yearly = help.validate_date(" Enter new annual fee last charged: ")
            if choice == 6:
                return
def main():
    #Create a subscription object
    # sub = Subscription.create()
    x = Subscription()
    x.edit_menu()
    Subscription.create()

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
            
    # json_string = sub.to_json()
    # print(json_string)
    # print("\n")
    # print(sub)
            
if __name__ == "__main__":
    main()
