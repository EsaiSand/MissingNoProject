import json
import helpers as help
from datetime import datetime as dt
from .._dependencies.dateutil.relativedelta import relativedelta 

class User:
    '''A class to represent a user with various attributes.

    Attributes:
        name (str): The name of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        income (float): The periodical income of the user.
        funds (float): The current funds available to the user.
        pay_schedule (str): The payment schedule (Monthly, Biweekly, or Weekly).
    '''
    
    PAY_INTS = {
        "Monthly": relativedelta(months=1),
        "Biweekly": relativedelta(weeks=2),
        "Weekly": relativedelta(weeks=1)
    }

    def __init__(self, name: str = "user", email: str = "", password: str = "password",
                 income: float = 0.0, funds: float = 0.0, pay_schedule: int = 0):
        '''Initializes a User object with default attributes if none are provided.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            income (float): The monthly income of the user.
            funds (float): The current funds available to the user.
            pay_schedule (str): The payment schedule(Monthly, Biweekly, or Weekly).
            last_pay_date: (date): The date of last pay day
        '''
        self.name = name
        self.email = email
        self.password = password
        self.income = income
        self.funds = funds
        self.pay_schedule = pay_schedule
        self.last_pay_date = dt.now()

    def set_username(self, username: str):
        '''Sets the username of the user.

        Args:
            username (str): The new username for the user.
        '''
        
        self.name = username
        return self.name

    def set_password(self, password: str):
        '''Sets the password of the user.

        Args:
            password (str): The new password for the user.
        '''
        self.password = password

    def set_email(self, email: str):
        '''Sets the email of the user.

        Args:
            email (str): The new email address for the user.
        '''
        self.email = email

    def set_income(self, income: float):
        '''Sets the income of the user.

        Args:
            income (float): The new monthly income for the user.
        '''
        self.income = income

    def set_pay_schedule(self, pay_schedule: int):
        '''Sets the payment schedule.

        Args:
            pay_schedule (int): The new payment schedule in days.
        '''
        self.pay_schedule = pay_schedule

    def get_funds(self):
        '''Returns the current funds available to the user.

        Returns:
            float: The amount of funds available.
        '''
        return self.funds

    def update_funds(self):
        '''Updates funds based on income and last pay date'''
        today = dt.now()
        next_pay_date = self.last_pay_date + User.PAY_INTS[self.pay_schedule]
        caught_up = next_pay_date > today
        while not caught_up:
            self.last_pay_date = next_pay_date
            self.funds += self.income

            next_pay_date += User.PAY_INTS[self.pay_schedule]
            caught_up = next_pay_date > today

    def __str__(self):
        '''Returns a string representation of the user.

        Returns:
            str: A string representing the user's attributes.
        '''
        info = (f"USER {self.name}:\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n"
                f"Income: ${self.income:.2f}\n"
                f"Funds: ${self.funds:.2f}\n"
                f"Pay Schedule: Every {self.pay_schedule} days")
    
        return f"~|{'Username': ^14}|{'email': ^20}|{'password': ^20}|{'Income': ^12}|{'Funds': ^12}|{'Pay Schedule': ^12}|{'Last Pay Day': ^15}|~\n||{self.name: ^14}|{self.email: ^20}|{'*' * len(self.password): ^20}|{self.income: ^12}|{self.funds: ^12}|{self.pay_schedule: ^12}|{self.last_pay_date.strftime(r'%x'): ^15}||"
    
    def to_json(self):
        '''
        Returns user object in json string representation 
        '''
        # Objects attributes stored in dictionary
        last = self.last_pay_date
        attr_dict = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "income": self.income,
            "funds": self.funds,
            "pay_schedule": self.pay_schedule,
            "last_pay_date": [last.strftime("%Y"), last.strftime("%m"), last.strftime('%d')]
        }

        json_format = json.dumps(attr_dict, indent=4)
        return json_format

    @staticmethod
    def from_json(json_string):
        '''
        Creates a static instance based on given json string following format
        of to_json() method's json string
        '''
        attr_dict = json.loads(json_string)

        obj = User()

        obj.name = attr_dict["name"]
        obj.email = attr_dict["email"]
        obj.password = attr_dict["password"]
        obj.income = attr_dict["income"]
        obj.funds = attr_dict["funds"]
        obj.pay_schedule = attr_dict["pay_schedule"]

        last = attr_dict["last_pay_date"]
        obj.last_pay_date = dt.date(int(last[0]), int(last[1]), int(last[2]))
        
        return obj
    
    @staticmethod
    def create():
        '''Creates custom instance of User by prompting for user input'''
        new_user = User()

        new_user.name = input("Provide a username: ")
        new_user.email = help.validate_input(" ", "Enter user email: ", regex=r"^.+@.+\..{3}")
        
        pass_checked = False
        password = ""
        while not pass_checked:
            first = input("Create account password: ")
            second = input("Re-enter account password: ")
            if first != second:
                print("Passwords do not match, try again")
            else:
                password = first
                pass_checked = True
        
        new_user.password = password
        new_user.funds = help.validate_input(0.0, "What are your current funds available for budgeting?(ex. $1233.05): $", pos=True)
        

        choice = help.validate_input(0, "What is your expected income period? (Ex. If paid every 2 weeks, select 2)\n1. Monthly\n2. Biweekly\n3. Weekly\nSelection: ", valids=[1,2,3])
        match choice:
            case 1:
                new_user.pay_schedule = "Monthly"
            case 2:
                new_user.pay_schedule = "Biweekly"
            case 3:
                new_user.pay_schedule = "Weekly"
    
        new_user.income = help.validate_input(0.0, "What is your expected income for every pay period?(If paid weekly, expected payment after every week): $", pos=True)
        new_user.income = help.validate_date("When was the last time you were paid?(MM-DD-YYYY): ", max_date=dt.now())

        return new_user

#vvv hould be moved into main file vvv
def main():
    # Create a User object with default values
    user = User()

    # Menu loop
    while True:
        print("\nOptions:")
        print("1. Set username")
        print("2. Set email")
        print("3. Set password")
        print("4. Set income")
        print("5. Set pay schedule")
        print("6. View user details")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ")

        if choice == "1":
            # Set username
            username = input("\nEnter the new username: ")
            user.set_username(username)
            print(f"Username set to: {user.name}")

        elif choice == "2":
            # Set email
            email = input("\nEnter the new email address: ")
            user.set_email(email)
            print(f"Email set to: {user.email}")

        elif choice == "3":
            # Set password
            password = input("\nEnter the new password: ")
            user.set_password(password)
            print(f"Password set successfully.")

        elif choice == "4":
            # Set income
            while True:
                try:
                    income = float(input("\nEnter the new income: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            user.set_income(income)
            print(f"Income set to: ${user.income:.2f}")

        elif choice == "5":
            # Set pay schedule
            while True:
                try:
                    pay_schedule = int(input("\nEnter the pay schedule in days: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            user.set_pay_schedule(pay_schedule)
            print(f"Pay schedule set to: Every {user.pay_schedule} days")

        elif choice == "6":
            # View user details
            print("\nUser Details:")
            print(user)

        elif choice == "7":
            # Exit the program
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
