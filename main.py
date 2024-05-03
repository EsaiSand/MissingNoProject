from classes.user_manager import UserManager
from classes.user import User
from classes.debt import Debt
import classes.helpers as help
import json

def login(users, user_name, user_password,):
  """Lets a user attempt to login to a user account"""

  #gets list of users from json file
  users = User.from_json()

  #checks if user is valid
  for i in range(len(users)):

    #if user is valid:
    if ( (user_name == users[i].username) and (user_password == users[i].password)):
      valid_user = users[i]
      break

  #returns a the user object that is the valid user 
  return valid_user
  

#The main function of the program
def main():
  '''Main function of the program. What runs the full code'''
  new_user = UserManager.startup()
  if new_user == 1:
    username = help.validate_input(str(), "Enter a Username: ")
    email = help.validate_input(str(), "Enter an Email Address: ")
    password = help.validate_input(str(), "Enter a Password: ")


  print(Debt())


if __name__ == "__main__":
  main()