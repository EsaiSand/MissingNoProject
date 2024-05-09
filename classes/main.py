from user_manager import UserManager
from user import User
from debt import Debt
import helpers as help
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
  # '''Main function of the program. What runs the full code'''
  pass

if __name__ == "__main__":
  main()