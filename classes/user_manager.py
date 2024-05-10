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

  def list_user(self):
    info = str(self.user)

  def list_debts(self):
    count = 0
    info = ""
    for debt in self.debts:
      debt_str = ""
      if(count == 0):
        debt_str = str(debt)
      else:
        debt_str = str(debt)
        end_title = debt_str.find("||")
        debt_str = debt_str[end_title:]

      count += 1
      info += debt_str
    
    return info
  
  def list_subs(self):
    count = 0
    info = ""
    for sub in self.subcriptions:
      sub_str = ""
      if(count == 0):
        sub_str = str(sub)
      else:
        sub_str = str(sub)
        end_title = sub_str.find("||")
        sub_str = sub_str[end_title:]

      count += 1
      info += sub_str
    
    return info
  
  def list_exps(self):
    count = 0
    info = ""
    for exp in self.expenses:
      exp_str = ""
      if(count == 0):
        exp_str = str(exp)
      else:
        exp_str = str(exp)
        end_title = exp_str.find("||")
        exp_str = exp_str[end_title:]

      count += 1
      info += exp_str
    
    return info
  
  def list_meals(self):
    count = 0
    info = ""
    for meal in self.meals:
      meal_str = ""
      if(count == 0):
        meal_str = str(meal)
      else:
        meal_str = str(meal)
        end_title = meal_str.find("||")
        meal_str = meal_str[end_title:]

      count += 1
      info += meal_str

  def list_ingrs(self):
    count = 0
    info = ""
    for ingr in self.ingredients:
      ingr_str = ""
      if(count == 0):
        ingr_str = str(ingr)
      else:
        ingr_str = str(ingr)
        end_title = ingr_str.find("||")
        ingr_str = ingr_str[end_title:]

      count += 1
      info += ingr_str

  def to_json(self):
    '''Stores all user data (from each class) into a single file'''

    #loops store all data object elements into a json list, which is stored
    debts_json = []
    for i in range(len(self.debts)):
      debts_json.append(self.debt[i].to_json())

    expenses_json = []
    for i in range(len(self.expenses)):
      expenses_json.append(self.expenses[i].to_json())

    subscriptions_json = []
    for i in range(len(self.subscriptions)):
      subscriptions_json.append(self.expenses[i].to_json())

    meals_json = []
    for i in range(len(self.meals)):
      meals_json.append(self.meals[i].to_json())

    ingredients_json = []
    for i in range(len(self.ingredients)):
      ingredients_json.append(self.ingredients[i].to_json())

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
  def from_json(json_string):
    '''grabs elements from json and and constructs/returns a usermanager object'''
    
    attr_dict = json.loads(json_string)

    new_userman = UserManager()

    str_user = attr_dict["User"]
    new_userman.user.from_json(str_user)

    lst_debts = attr_dict["Debts"]
    for debts in lst_debts:
      new_userman.debts.append(Debt().from_json(debts))

    lst_expenses = attr_dict["Expenses"]
    for expenses in lst_expenses:
      new_userman.expenses.append(Expense().from_json(expenses))

    lst_subcriptions = attr_dict["Subscriptions"]
    for subscriptions in lst_subcriptions:
      new_userman.subcriptions.append(Subscription().from_json(subscriptions))

    lst_meals = attr_dict["Meals"]
    for meal in lst_meals:
      new_userman.meals.append(Meal().from_json(meal))

    lst_ingredients = attr_dict["Ingredients"]
    for ingredient in lst_ingredients:
      new_userman.ingredients.append(Ingredients().from_json(ingredient))

    return new_userman
  
  def create_obj(self, obj):
    '''
    passes in an object type and create an object based what object is passed to it
    '''
    """
    What would you like to do?
    > create obj
    > update obj
    > remove obj

    if create obj:
      obj.create()
    elif update obj:
      obj.update
    else:
      remove object from self.obj list
    """

    inpt = help.validate_input(0, "What would you like to do? \n1. Create \n2. Update \n3.remove", valids=[1,2,3])
    if inpt == 1:
      obj().create()
    #this will need to be set, not update. Don't know if this one will work either, This might be used in main
    if inpt == 2:
      obj().update()
    #Idk if this works
    if inpt == 3:
      for obj in self.obj:
        self.obj.remove(obj)


def main():
  pass

if __name__ == "__main__":
    main()
