from user_manager import UserManager
from user import User
from debt import Debt
from expense import Expense
from ingredient import Ingredients
from meal import Meal
from subscription import Subscription
import helpers as help
import json

def boot_up():
  '''Function to start running program'''
  print("--------------------Welcome to Budget Manager--------------------\n")

  # Loads data from text file
  f = open("../data/data.txt")
  data_string = f.read()
  f.close()

  # Dictionary pairing all users with user_manager json strings
  users_lib = {}

  # Fills users_lib if there  are stored users in data file
  if(len(data_string) != 0):
    users_lib = json.loads(data_string)

  user_num = -1   # Tracks index of 'focused' user_manager
  manager = None # Tracks 'focused' user_manager
  user_count = 0 # Tracks total amount of users in storage

  while True:
    # Counts amount of users if there where any to begin with
    user_count = 0
    if users_lib != None:
      for user in users_lib:
        user_count += 1

    # Main menu
    choice = help.validate_input(1, "\nSelect from the following:\n1. Log in\n2. Create new account\n3. Quit\n\nSelection: ", valids=[1,2,3])

    # Chose to login
    if choice == 1:
      print("\n----Logging in----")
      manager, user_num = login(users_lib)
    # Chose to create user
    if choice == 2:
      print("\n----Creating new account----")
      manager, user_num = create_user_manager(user_count)
      user_count += 1
      user_name = f"User {user_num}"
      users_lib[user_name] = manager.to_json()
      save_users(users_lib)
    # Chose to quit
    if choice == 3:
      print("Quitting")
      break

    # If we've logged into existing user, or created new user, enter user menu
    if(manager != None):
      manager = handle_user(manager)

      # Once exiting user menu, save / overwrite user in user_libs for storage
      user_name = f"User {user_num}"
      users_lib[user_name] = manager.to_json()
      save_users(users_lib)

  # Saving user data when quitting
  save_users(users_lib)

def save_users(all_managers):
  '''
  Saves all_managers to data file
  '''
  storage = json.dumps(all_managers, indent=4)
  f = open("../data/data.txt", "w")
  f.write(storage)
  f.close()
  return storage

def login(users_lib):
  '''Attempts login and when valid, returns corrseponding user_manager
  Returns user_manager instance of corresponding credentials user
  and index of user manager in users_lib'''

  # If no instances in data, cannot login
  if not users_lib:
    print('\nThere are no users yet!\n')
    return [None, 0]
  
  # Otherwise, there are instances in data, attempt a login
  ums_list = [] # List of instantiated user managers

  # Instantiate user managers from users_lib
  for user in users_lib:
    # Getting json strig of current user_manager
    um_json = users_lib[user]
    Debt.DEBT_COUNT = 0
    # Creating user objects from data and appends to user list
    um_instance = UserManager.from_json(um_json)
    ums_list.append(um_instance)
  # Now have full list of all user managers instantiated

  # Attempting login
  while True:
    print("\nType 'back' to go back to main menu")
    username = input("Username: ")
    if(username == "back"):
      return [None, -1]
    
    # Looking for user with matching username
    target = -1
    for i in range(len(ums_list)):
      if ums_list[i].user.name == username:
        target = i
        break

    # Case when no user matches username given
    if target == -1:
      print(f"User with username '{username}' does not exist! Try again")
      continue

    # At this point, username was valid, corresponding user pointed at by target
    target_manager = ums_list[target]
    while True:
      # Prompts for password to target user
      print("\nType 'back' to go back to username")
      password = input("Password: ")
      if password == "back":
        break
      
      if target_manager.user.password == password:
        return [target_manager, target]

    # for i in range(len(ums_list)):
    #   # User obj found with matching username
    #   if ums_list[i].user.name == username:
    #     print("\nType 'back' to go back to username")
    #     password = input("Password: ")
    #     if password == "back":
    #       break
    #     # If username and password match, we've found right user_manager
    #     if ums_list[i].user.password == password:
    #       return [ums_list[i], i]
    #     else:
    #       print("Password does not match!\n")
    #   else:
    #     # When through all of users without finding matching username
    #     print("Username does not exist!\n")  
  
def create_user_manager(user_counts):
  '''Creates new user manager instance by first instantiating User'''
  new_manager = UserManager()
  new_manager.user = User.create()
  return [new_manager, user_counts]

def handle_user(u_manager):
  '''Menu for interacting with connected user manager'''
  print(f"\n\nWelcome, {u_manager.user.name}")

  # Entering menu loop
  while True:
    choice = help.validate_input(1, "\nSelect one of the following:\n1. Edit account/data\n2. View account/data\n3. Generate holistic report\n4. Logout\nSelection: ", valids=[1,2,3,4])
    # Chose to edit
    if choice == 1:
      # EDITING
      while True:
        choice = help.validate_input(1, "\nSelect one of the following edits\n1. Edit account details\n2. Edit debts\n3. Edit expenses\n4. Edit subscriptions\n5. Edit meals\n6. Edit ingredients\n7. Edit spending limit\n8. Exit editing\nSelection: ", valids=[1,2,3,4,5,6,7,8])

        # Chose to edit account
        if choice == 1:
          print("\nEditing account")
          u_manager.user_menu()
        # Chose to edit debts
        if choice == 2:
          print("\nEditing debts")
          u_manager.debt_menu()
        # Chose to edit expenses
        if choice == 3:
          print("\nEditing expenses")
          u_manager.expense_menu()
        # Chose to edit subscriptions
        if choice == 4:
          print("\nEditing subscriptions")
          u_manager.subscription_menu() 
        # Chose to edit meals
        if choice == 5:
          print("\nEditing meals")
          u_manager.meal_menu()
        # Chose to edit ingredients
        if choice == 6:
          print("\nEditing ingredients")
          u_manager.ingredients_menu
        # Chose to edit spending limit
        if choice == 7:
          u_manager.set_spending_limit()
        # Chose to exit
        if choice == 8:
          print("\nExiting edit mode")
          break

    # Chose to view
    if choice == 2:
      while True:
        choice = help.validate_input(1, "\nSelect one of the following records to view:\n1. User details\n2. Debts\n3. Expenses\n4. Subscriptions\n5. Meals\n6. Ingredients\n7. Spending limit\n8. Exit viewing mode\nSelection: ", valids=[1,2,3,4,5,6,7,8])
        # Chose to view account
        if choice == 1:
          print("\nAccount details:")
          u_manager.list_user()
        # Chose to view debts
        if choice == 2:
          print("\nUser debts:")
          u_manager.list_debts()
        # Chose to view expenses
        if choice == 3:
          print("\nUser expenses:")
          u_manager.list_exps()
        # Chose to view subscriptions
        if choice == 4:
          print("\nUser subscriptions:")
          u_manager.list_subs()
        # Chose to view meals
        if choice == 5:
          print("\nUser meals:")
          u_manager.list_meals()
        # Chose to view ingredients
        if choice == 6:
          print("\nUser ingredients:")
          u_manager.list_ingrs()
        # Chose to view spending limit
        if choice == 7:
          print("\nUser monthly spending limit: ")
          print(f"${u_manager.spending_limit}")
        # Chose to exit
        if choice == 8:
          print("\nExiting edit mode")
          break

    # Chose quick report
    if choice == 3:
      pass

    # Chose to exit
    if choice == 4:
      print("\nLogging out...")
      break
  
  return u_manager




#The main function of the program
def main():
  '''Main function of the program. What runs the full code'''
  boot_up()



if __name__ == "__main__":
  main()