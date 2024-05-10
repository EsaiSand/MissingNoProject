from debt import Debt
from expense import Expense
from ingredient import Ingredients
from meal import Meal
from subscription import Subscription
from user import User
import helpers as help
import json

class UserManager:
  '''User manager represents a user acccount:
  It controls the connection between a User object and its
  associated debt/expense/etc. objects. UserManager is where a user will
  edit their data / request reports'''

  def __init__(self):
    self.user = User()
    self.debts = []
    self.expenses = []
    self.subscriptions = []
    self.meals = []
    self.ingredients = []
    self.spending_limit = 0.0

  def list_user(self):
    info = str(self.user)
    return info

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
    for sub in self.subscriptions:
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
      "Ingredients": ingredients_json,
      "Spending Limit": self.spending_limit
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
      new_userman.subscriptions.append(Subscription().from_json(subscriptions))

    lst_meals = attr_dict["Meals"]
    for meal in lst_meals:
      new_userman.meals.append(Meal().from_json(meal))

    lst_ingredients = attr_dict["Ingredients"]
    for ingredient in lst_ingredients:
      new_userman.ingredients.append(Ingredients().from_json(ingredient))

    new_userman.spending_limit = attr_dict["Spending Limit"]

    return new_userman
  
  def set_spending_limit(self):
    '''has the user create a spending limit for themselves.'''
    self.spending_limit = help.validate_input(0.0, "What is the limit you are willing to spend this month?: $")
    return self.spending_limit

  def get_budget(self):
    '''gets the budget the user has created and compares it to the ammount they have spent that month'''

    total_spending = 0.0
    for i in range(len(self.expenses)):
      total_spending += self.expenses[i].cost
    
    if total_spending >= self.spending_limit:
      return f"Your budget was ${self.spending_limit}. \nYou spent ${total_spending - self.spending_limit} over budget!"
    else:
      return f"Your budget was ${self.spending_limit}. \nYou spent ${total_spending - self.spending_limit} under budget!"

  def user_menu(self):
    '''creates a menu to select and call different user menus options'''
     
    print("Here is a list of your current user information:")
    print(self.list_user())

    #edit
    print("which subscription record would you like to edit?")
    self.user.edit_menu()

  def debt_menu(self):
    '''creates a menu to select and call different debt menus options'''

    print("Here is a list of all debt records:")
    print(self.list_debts())
    
    print("What would you like to do? \n1. create. \n2. edit \n3. delete")
    options = help.validate_input(0, "Please select an option (1/2): ", valids=[1,2,3])

    #add
    if options == 1:
      self.debts.append(Debt.create())
    
    #edit
    if options == 2:
      print("which debt record would you like to edit?")
      choice = help.validate_input(0, "Pick a number from the list of debts: " , range(1 , len(self.debts) + 1))
      self.debts[choice - 1].edit_menu()

    #delete
    if options == 3:
      print("Which debt record would you like to delete?")
      choice = help.validate_input(0, "Pick a number from the list of debts: " , range(1 , len(self.debts) + 1))
      check = help.validate_input('a', "are you sure?: (y/n)", valids=['y','n'])
      if check.lower() == 'y':
        self.debts.pop(choice-1)
      else:
        self.debt_menu()

  def expense_menu(self):
    '''creates a menu to select and call different expense menus options'''
    
    print("Here is a list of all current expenses:")
    print(self.list_exps())
    
    print("What would you like to do? \n1. create. \n2. edit \n3. delete")
    options = help.validate_input(0, "Please select an option (1/2/3): ", valids=[1,2,3])

    #add
    if options == 1:
      self.expenses.append(Expense.create())

    #edit
    if options == 2:
      print("which expense record would you like to edit?")
      choice = help.validate_input(0, "Pick a number from the list of expenses: " , range(1 , len(self.expenses) + 1))
      self.expenses[choice - 1].edit_menu()

    #remove
    if options == 3:
      print("Which expense record would you like to delete?")
      choice = help.validate_input(0, "Pick a number from the list of expenses: " , range(1 , len(self.expense) + 1))
      check = help.validate_input('a', "are you sure?: (y/n)", valids=['y','n'])
      if check.lower() == 'y':
        self.expenses.pop(choice-1)
      else:
        self.expense_menu()

  def subscription_menu(self):
    '''creates a menu to select and call different subscription menus options'''
     
    print("Here is a list of all current subscriptions:")
    print(self.list_subs())
    
    print("What would you like to do? \n1. create. \n2. edit \n3. delete")
    options = help.validate_input(0, "Please select an option (1/2/3): ", valids=[1,2,3])

    #add
    if options == 1:
      self.subscriptions.append(Subscription.create())

    #edit
    if options == 2:
      print("which subscription record would you like to edit?")
      choice = help.validate_input(0, "Pick a number from the list of subscriptions: " , range(1 , len(self.subscriptions) + 1))
      self.subscriptions[choice - 1].edit_menu()

    #remove
    if options == 3:
      print("Which subscription record would you like to delete?")
      choice = help.validate_input(0, "Pick a number from the list of subscriptions: " , range(1 , len(self.subscriptions) + 1))
      check = help.validate_input('a', "are you sure?: (y/n)", valids=['y','n'])
      if check.lower() == 'y':
        self.subscriptions.pop(choice-1)
      else:
        self.subscription_menu()

  def meal_menu(self):
    '''creates a menu to select and call different meal menus options'''
     
    print("Here is a list of all current meal: ")
    print(self.list_meals())
    
    print("What would you like to do? \n1. create. \n2. edit \n3. delete")
    options = help.validate_input(0, "Please select an option (1/2/3): ", valids=[1,2,3])

    #add
    if options == 1:
      self.meals.append(Meal.create())

    #edit
    if options == 2:
      print("which meal record would you like to edit?")
      choice = help.validate_input(0, "Pick a number from the list of meals: " , range(1 , len(self.meals) + 1))
      self.meals[choice - 1].edit_menu()

    #remove
    if options == 3:
      print("Which meal record would you like to delete?")
      choice = help.validate_input(0, "Pick a number from the list of meals: " , range(1 , len(self.meals) + 1))
      check = help.validate_input('a', "are you sure?: (y/n)", valids=['y','n'])
      if check.lower() == 'y':
        self.meals.pop(choice-1)
      else:
        self.meal_menu()

  def ingredients_menu(self):
    '''creates a menu to select and call different ingredient menu options'''
     
    print("Here is a list of all current ingriedients:")
    print(self.list_ingrs())
    
    print("What would you like to do? \n1. create. \n2. edit \n3. delete")
    options = help.validate_input(0, "Please select an option (1/2/3): ", valids=[1,2,3])

    #add
    if options == 1:
      self.ingredients.append(Ingredients.create())

    #edit
    if options == 2:
      print("which ingredient record would you like to edit?")
      choice = help.validate_input(0, "Pick a number from the list of ingredients: " , range(1 , len(self.ingredients) + 1))
      self.ingredients[choice - 1].edit_menu()

    #remove
    if options == 3:
      print("Which ingredient record would you like to delete?")
      choice = help.validate_input(0, "Pick a number from the list of ingredients: " , range(1 , len(self.ingredients) + 1))
      check = help.validate_input('a', "are you sure?: (y/n)", valids=['y','n'])
      if check.lower() == 'y':
        self.ingredients.pop(choice-1)
      else:
        self.ingredients_menu()

def main():
  pass
if __name__ == "__main__":
    main()
