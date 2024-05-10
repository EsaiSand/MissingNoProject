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
  # Loads data from text file
  f = open("../data/data.txt")
  data_string = f.read()
  f.close()
  users_lib = None
  if(len(data_string) != 0):
    users_lib = json.loads(data_string)

  print("--------------------Welcome to Budget Manager--------------------\n\nAt any point, type to 'back' to go back if selection not available\n")

  user_num = 0
  manager = None

  while True:
    user_count = 0

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
      save_user(manager,user_num, users_lib)
    if choice == 3:
      print("Quitting")
      break

    if(manager != None):
      handle_user(manager)
  
  if manager == None:
    return

  # Saving user data when quitting
  save_user(manager, user_num, users_lib)

def save_user(u_manager, u_num, all_managers):
  '''Stores complete user data and updates user_manager defined by u_num with u_manager
  u_manager: User manger that has been open and potentially edited
  u_num: Position of u_manager in mega data
  all_managers: dictionary holding data of all user managers
  '''
  updated_manager_json = u_manager.to_json()
  users_managers = {} # Will be dict of updated user mangers json strings to store
  count = 0
  # For each user stored in data, create corresponding user manger
  for user in all_managers:
    user_id = "User " + str(count)
    # If looking at user manager pointed at u_num, replace with updated u_manager
    if count == u_num:
      users_managers[user_id] = updated_manager_json
    else:
      users_managers[user_id] = user

  storage = json.dumps(users_managers, indent=4)
  f = open("../data/data.txt")
  f.write(storage)
  f.close()
  return storage

def login(data_str):
  '''Attempts login and when valid, returns corrseponding user_manager'''
  total_users = 0

  # If no instances in data, cannot login
  if(len(data_str) == 0):
    print('\nThere are no users yet!\n')
    return [None, 0]
  
  # Otherwise, there are instances in data, attempt a login
  ums_list = [] # List of instantiated user managers
  users_lib = json.loads(data_str) # Dict storing json of all user managers stored

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
  new_manager.user = User.create()
  return [new_manager, user_counts+1]

def handle_user(u_manager):
  pass


#The main function of the program
def main():
  '''Main function of the program. What runs the full code'''
  boot_up()



if __name__ == "__main__":
  main()