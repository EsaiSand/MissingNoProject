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
  manager = UserManager()

  print("--------------------Welcome to Budget Manager--------------------\n\nAt any point, type to 'back' to go back if selection not available\n")
  
  manager = None
  user_num = 0

  while True:
    choice = help.validate_input(1, "Select from the following:\n1. Log in\n2. Create new account\n3. Quit\nSelection: ", valids=[1,2,3])

    if choice == 1:
      manager, user_num = login(data_string)
    if choice == 2:
      manager, user_num = create_user_manager()
    if choice == 3:
      break

    if(manager != None):
      handle_user(manager)
  
  # Saving user data when quitting
  save_user(manager, user_num, data_string)

def save_user(u_manager, u_num, old_data_str):
  '''Stores complete user data and updates user_manager defined by u_num with u_manager
  u_manager: User manger that has been open and potentially edited
  u_num: Position of u_manager in mega data
  old_data_str: json_string of mega data before u_manager was opened and maybe changed
  '''
  # Creates complete user dict from old_data_str
  users_dict = json.loads(old_data_str)
  users_managers = [] # Will be list of fully instantiated user mangers defined in storage

  # For each user stored in data, create corresponding user manger
  for user in users_dict:
    manager = UserManager()
    manager_instance_dict = UserManager.from_json(users_dict[user])
    manager.user = User.from_json(manager_instance_dict["User"])

    # Creating Debt objects from data
    debts_list = json.loads(manager_instance_dict["Debts"])
    for debt_string in debts_list:
      new_debt = Debt.from_json(debt_string)
      manager.debts.append(new_debt)

    # Creating Expense objects from data
    expenses_list = json.loads(manager_instance_dict["Expenses"])
    for expense_string in expenses_list:
      new_expense = Expense.from_json(expense_string)
      manager.expenses.append(new_expense)

    # Creating Subscriptions objects from data
    subs_list = json.loads(manager_instance_dict["Subscriptions"])
    for sub_string in subs_list:
      new_sub = Subscription.from_json(sub_string)
      manager.subcriptions.append(new_sub)

    # Creating Meals objects from data
    meals_list = json.loads(manager_instance_dict["Meals"])
    for meal_string in meals_list:
      new_meal = Meal.from_json(meal_string)
      manager.meals.append(new_meal)

    # Creating Ingredient objects from data
    ingrs_list = json.loads(manager_instance_dict["Ingredients"])
    for ing_string in ingrs_list:
      new_ingr = Ingredients.from_json(ing_string)
      manager.ingredients.append(new_ingr)

    # Append user manager to list of user managers
    users_managers.append(manager)

  # Now have a list of fully developed user managers
  meta_json = ''
  for i in range(len(users_managers)):
    if i == u_num 

def login(data_str):
  '''Attempts login and when valid, returns corrseponding user_manager'''
  total_users = 0

  # If no instances in data, cannot login
  if(len(data_str) == 0):
    print('\nThere are no users yet!\n')
    return [None, 0]
  # If there are instances in data, attempt a login
  else:
    user_list = []
    user_managers_dict = json.loads(data_str)

    # Instantiate only user objects for all users
    for user in user_managers_dict:
      # Creating dictionary representing user instance (contains User, Debts, Subs, ...)
      user_data_string = user_managers_dict[user]
      user_manager_instance = UserManager.from_json(user_data_string)
      users_dict = User.from_json(user_data_string)
      total_users += 1
      # Creating user objects from data and appends to user list
      user_list.append(User.from_json(users_dict["User"]))

    # Attempting login
    while True:
      username = input("Username: ")
      if(username == "back"):
        return None
      
      target = 0
      for i in range(len(user_list)):
        # User obj found with matching username
        if user_list[i].name == username:
          target = i
          password = input("Password: ")
          if password == "back":
            break
          # If username and password match, create rest of UserManager
          if user_list[i].password == password:
            manager = UserManager()
            manager.user = user_list[i]
            # Creating Debts objects from data
            debts_list = json.loads(users_dict["Debts"])
            for debt_string in debts_list:
              new_debt = Debt.from_json(debt_string)
              manager.debts.append(new_debt)

            # Creating Expense objects from data
            expenses_list = json.loads(users_dict["Expenses"])
            for expense_string in expenses_list:
              new_expense = Expense.from_json(expense_string)
              manager.expenses.append(new_expense)

            # Creating Subscriptions objects from data
            subs_list = json.loads(users_dict["Subscriptions"])
            for sub_string in subs_list:
              new_sub = Subscription.from_json(sub_string)
              manager.subcriptions.append(new_sub)

            # Creating Meals objects from data
            meals_list = json.loads(users_dict["Meals"])
            for meal_string in meals_list:
              new_meal = Meal.from_json(meal_string)
              manager.meals.append(new_meal)

            # Creating Ingredient objects from data
            ingrs_list = json.loads(users_dict["Ingredients"])
            for ing_string in ingrs_list:
              new_ingr = Ingredients.from_json(ing_string)
              manager.ingredients.append(new_ingr)

            return manager
          else:
            print("Password does not match!\n")
        
        # When through all of users without finding matching username
        print("Username does not exist!\n")  
              

  users_dict = json.loads(data_string)
  print(type(users_dict))

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
  
def create_user_manager():
  '''Creates new user manager instance by first instantiating User'''
  new_manager = UserManager()
  new_manager.user = User.create()
  return new_manager

def handle_user(u_manager):
  pass


#The main function of the program
def main():
  # '''Main function of the program. What runs the full code'''
  boot_up("1","","")

if __name__ == "__main__":
  main()