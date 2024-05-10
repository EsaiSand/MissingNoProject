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
  print("--------------------Welcome to Budget Manager--------------------\n\nAt any point, type to 'back' to go back if selection not available\n")

  # Loads data from text file
  f = open("../data/data.txt")
  data_string = f.read()
  f.close()

  # Dictionary pairing all users with user_manager json strings
  users_lib = {}

  # Fills users_lib if there  are stored users in data file
  if(len(data_string) != 0):
    users_lib = json.loads(data_string)

  user_num = 0   # Tracks index of 'focused' user_manager
  manager = None # Tracks 'focused' user_manager

  while True:
    user_count = 0 # Tracks total amount of users to store

    # Counts amount of users if there where any to begin with
    if users_lib != None:
      for user in users_lib:
        user_count += 1

    choice = help.validate_input(1, "Select from the following:\n1. Log in\n2. Create new account\n3. Quit\nSelection: ", valids=[1,2,3])

    if choice == 1:
      print("Logging in")
      manager, user_num = login(data_string)

    if choice == 2:
      print("Creating new account")
      manager, user_num = create_user_manager(user_count)
      user_name = f"User {user_num}"
      users_lib[user_name] = manager.to_json()
      save_users(users_lib)

    if choice == 3:
      print("Quitting")
      break

    if(manager != None):
      handle_user(manager)
      user_name = f"User {user_num}"
      users_lib[user_name] = manager.to_json()
      save_users(users_lib)
  
  if manager == None:
    return

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
  '''Attempts login and when valid, returns corrseponding user_manager'''
  total_users = 0

  # If no instances in data, cannot login
  if not users_lib:
    print('\nThere are no users yet!\n')
    return [None, 0]
  
  # Otherwise, there are instances in data, attempt a login
  ums_list = [] # List of instantiated user managers

  # Instantiate only user objects for all users
  for user in users_lib:
    # Creating dictionary representing user instance (contains User, Debts, Subs, ...)
    um_json = users_lib[user]
    Debt.DEBT_COUNT = 0
    um_instance = UserManager.from_json(um_json)
    total_users += 1
    # Creating user objects from data and appends to user list
    ums_list.append(um_instance)
  # Now have full list of all user managers instantiated

  # Attempting login
  while True:
    username = input("Username: ")
    if(username == "back"):
      return None
    
    target = 0
    for i in range(len(ums_list)):
      # User obj found with matching username
      if ums_list[i].user.name == username:
        target = i
        password = input("Password: ")
        if password == "back":
          break
        # If username and password match, create rest of UserManager
        if ums_list[i].user.password == password:
          return [ums_list[i], i]
        else:
          print("Password does not match!\n")
      
      # When through all of users without finding matching username
      print("Username does not exist!\n")  
  
def create_user_manager(user_counts):
  '''Creates new user manager instance by first instantiating User'''
  new_manager = UserManager()
  new_manager.user = User()
  return [new_manager, user_counts+1]

def handle_user(u_manager):
  pass

#The main function of the program
def main():
  '''Main function of the program. What runs the full code'''
  boot_up()



if __name__ == "__main__":
  main()