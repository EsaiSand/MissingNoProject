from user_manager import UserManager
from user import User
from debt import Debt
from expense import Expense
from ingredient import Ingredients
from meal import Meal
from subscription import Subscription
import helpers as help
import json

def boot_up(users, user_name, user_password,):
  """Function to start running program"""
  # Loads data from text file
  data_string = open("../data/data.txt").read()
  users = {}
  manager = UserManager()

  print("--------------------Welcome to Budget Manager--------------------\n\n")
  choice = help.validate_input(1, "Select from the following:\n1. Log in\n2. Create new account\n3. Quit\nSelection: ", valids=[1,2,3])


  # If now instances in data, start by creating new user
  if(len(data_string) == 0):
    manager = create_user()
  # If there are instances in data, attempt a login
  else:
    users = json.loads(data_string)
    for user in users:
      pass
      # # Creating dictionary representing user instance (contains User, Debts, Subs, ...)
      # user_data_string = users[user]
      # user_data = User.from_json(user_data_string)

      # # Creating user objects from data
      # manager.user = User.from_json(user_data["User"])

      # # Creating Debts objects from data
      # debts_list = json.loads(user_data["Debts"])
      # for debt_string in debts_list:
      #   new_debt = Debt.from_json(debt_string)
      #   manager.debts.append(new_debt)

      # # Creating Expense objects from data
      # expenses_list = json.loads(user_data["Expenses"])
      # for expense_string in expenses_list:
      #   new_expense = Expense.from_json(expense_string)
      #   manager.expenses.append(new_expense)

      # # Creating Subscriptions objects from data
      # subs_list = json.loads(user_data["Subscriptions"])
      # for sub_string in subs_list:
      #   new_sub = Subscription.from_json(sub_string)
      #   manager.subcriptions.append(new_sub)

      # # Creating Meals objects from data
      # meals_list = json.loads(user_data["Meals"])
      # for meal_string in meals_list:
      #   new_meal = Meal.from_json(meal_string)
      #   manager.meals.append(new_meal)

      # # Creating Ingredient objects from data
      # ingrs_list = json.loads(user_data["Ingredients"])
      # for ing_string in ingrs_list:
      #   new_ingr = Ingredients.from_json(ing_string)
      #   manager.ingredients.append(new_ingr)


  user_dict = json.loads(data_string)
  print(type(user_dict))

  # #gets list of users from json file
  # users = User.from_json()

  # #checks if user is valid
  # for i in range(len(users)):

  #   #if user is valid:
  #   if ( (user_name == users[i].username) and (user_password == users[i].password)):
  #     valid_user = users[i]
  #     break

  # #returns a the user object that is the valid user 
  # return valid_user
  
def create_user():
  pass

def login():
  pass


#The main function of the program
def main():
  # '''Main function of the program. What runs the full code'''
  boot_up("1","","")

if __name__ == "__main__":
  main()