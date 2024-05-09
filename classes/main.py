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
  '''Function to start running program'''
  # Loads data from text file
  data_string = open("../data/data.txt").read()
  users = {}
  manager = UserManager()

  print("--------------------Welcome to Budget Manager--------------------\n\nAt any point, type to 'back' to go back\n")
  
  while True:
    choice = help.validate_input(1, "Select from the following:\n1. Log in\n2. Create new account\n3. Quit\nSelection: ", valids=[1,2,3])

    if choice == 1:
      manager = login(data_string)
    if choice == 2:
      create_user()
    if choice == 3:
      break
  
def login(data_str):
  '''Attempts login and when valid, enters user loop'''
  while True:
    # If no instances in data, start by creating new user
    if(len(data_str) == 0):
      print('\nThere are no users yet!\n')
      return
    # If there are instances in data, attempt a login
    else:
      user_list = []
      users = json.loads(data_str)

      # Instantiate only user objects for all users
      for user in users:
        # Creating dictionary representing user instance (contains User, Debts, Subs, ...)
        user_data_string = users[user]
        user_data = User.from_json(user_data_string)

        # Creating user objects from data
        user_list.append(User.from_json(user_data["User"]))

      # Attempting login
      while True:
        username = input("Username: ")
        if(username == "back"):
          return None
        
        target = 0
        for i in range(user_list):
          # User obj found with matching username
          if user_list[i].name == username:
            password = input("Password: ")
            if password == "back":
              break

            if user_list[i].password == password:
              manager = UserManager()
              manager.user = user_list[i]
              # If username and password match, create rest of UserManager
              # Creating Debts objects from data
              debts_list = json.loads(user_data["Debts"])
              for debt_string in debts_list:
                new_debt = Debt.from_json(debt_string)
                manager.debts.append(new_debt)

              # Creating Expense objects from data
              expenses_list = json.loads(user_data["Expenses"])
              for expense_string in expenses_list:
                new_expense = Expense.from_json(expense_string)
                manager.expenses.append(new_expense)

              # Creating Subscriptions objects from data
              subs_list = json.loads(user_data["Subscriptions"])
              for sub_string in subs_list:
                new_sub = Subscription.from_json(sub_string)
                manager.subcriptions.append(new_sub)

              # Creating Meals objects from data
              meals_list = json.loads(user_data["Meals"])
              for meal_string in meals_list:
                new_meal = Meal.from_json(meal_string)
                manager.meals.append(new_meal)

              # Creating Ingredient objects from data
              ingrs_list = json.loads(user_data["Ingredients"])
              for ing_string in ingrs_list:
                new_ingr = Ingredients.from_json(ing_string)
                manager.ingredients.append(new_ingr)

              return manager
            else:
              print("Password does not match!\n")
        
        # When through all of users without finding matching username
        print("Username does not exist!\n")  
              

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
  new_manager = UserManager()
  new_manager.user = User.create()
  pass




#The main function of the program
def main():
  # '''Main function of the program. What runs the full code'''
  boot_up("1","","")

if __name__ == "__main__":
  main()