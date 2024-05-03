import json
import helpers as help

class User:
    '''A class to represent a user with various attributes.

    Attributes:
        name (str): The name of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        income (float): The monthly income of the user.
        funds (float): The current funds available to the user.
        pay_schedule (int): The payment schedule (e.g., days between payments).
    '''
    
    def __init__(self, name: str = "user", email: str = "", password: str = "password",
                 income: float = 0.0, funds: float = 0.0, pay_schedule: int = 0):
        '''Initializes a User object with default attributes if none are provided.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            income (float): The monthly income of the user.
            funds (float): The current funds available to the user.
            pay_schedule (int): The payment schedule in days.
        '''
        self.name = name
        self.email = email
        self.password = password
        self.income = income
        self.funds = funds
        self.pay_schedule = pay_schedule

    def set_username(self, username: str):
        '''Sets the username of the user.

        Args:
            username (str): The new username for the user.
        '''
        
        self.name = username

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

    def __str__(self):
        '''Returns a string representation of the user.

        Returns:
            str: A string representing the user's attributes.
        '''
        return (f"USER {self.name}:\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n"
                f"Income: ${self.income:.2f}\n"
                f"Funds: ${self.funds:.2f}\n"
                f"Pay Schedule: Every {self.pay_schedule} days")
    
    def to_json(self):
        '''
        Returns user object in json string representation 
        '''
        # Objects attributes stored in dictionary
        attr_dict = {
            "name": self.name,
            "email": self.amount,
            "password": self.amount,
            "income": self.is_compound,
            "funds": self.int_period,
            "pay_schedule": self.pay_schedule,
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

        return obj

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
