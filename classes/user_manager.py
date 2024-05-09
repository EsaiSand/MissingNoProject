from debt import Debt
from expense import Expense
from ingredient import Ingredients
from meal import Meal
from subscription import Subscription
from user import User
import helpers as help
import json

def main():
  UserManager.startup()

class UserManager:
  '''User manager represents a user acccount:
  It controls the connection between a User object and its
  associated debt/expense/etc. objects. UserManager is where a user will
  edit their data / request reports'''

  def __init__(self):
    self.user = User()
    self.debts = []
    self.expenses = []
    self.subcriptions = []
    self.meals = []
    self.ingredients = []

  @staticmethod
  def startup():
    """
    Prompts the User for login credentials or account creation to instantiate a user manager
    """
    print("Select one of the following:")
    print("1. Create new account")
    print("2. Login to existing account")
    inpt = help.validate_input(0, "Selection(1/2): ", valids=[1,2])
    

    # Account creation process
    if inpt == 1:
      user = User.create()
      user.subscriptions = Subscription.create()
    # Account login proccess
    else:
      pass

  def user_storage(self):
    '''Stores all user data (from each class) into a single file'''

    #loops store all data object elements into a json list, which is stored
    debts_json = []
    for i in range(len(self.debts)):
      debts_json[i].append(self.debt[i].to_json())

    expenses_json = []
    for i in range(len(self.expenses)):
      expenses_json[i].append(self.expenses[i].to_json())

    subscriptions_json = []
    for i in range(len(self.subscriptions)):
      subscriptions_json[i].append(self.expenses[i].to_json())

    meals_json = []
    for i in range(len(self.meals)):
      meals_json[i].append(self.meals[i].to_json())

    ingredients_json = []
    for i in range(len(self.ingredients)):
      ingredients_json[i].append(self.ingredients[i].to_json())

    #creates a dictionary of all the json strings and stores them in a dictionary
    attr_dict = {
      "User": self.user.to_json(),
      "Debts": debts_json,
      "Expenses": expenses_json,
      "Subscriptions": subscriptions_json,
      "Meals": meals_json,
      "Ingredients": ingredients_json
    }
    json_format = json.dumps(attr_dict, indent=4)
    return json_format

  @staticmethod
  def get_user(json_string):
    '''grabs elements from json and and constructs/returns a usermanager object'''
    
    attr_dict = json.loads(json_string)

    new_userman = UserManager()

    new_userman.user = attr_dict["User"]
    new_userman.debts = attr_dict["Debts"]
    new_userman.expenses = attr_dict["Expenses"]
    new_userman.subcriptions = attr_dict["Subscriptions"]
    new_userman.meals = attr_dict["Meals"]
    new_userman.ingredients = attr_dict["Ingredients"]
    Expense.CATEGORIES = attr_dict["Expense Categories"]

    return new_userman

if __name__ == "__main__":
    main()
