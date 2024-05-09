from debt import Debt
from expense import Expense
from ingredient import Ingredients
from meal import Meal
from subscription import Subscription
from user import User
import helpers as help

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


if __name__ == "__main__":
    main()
