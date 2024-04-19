from ingredient import Ingredients

class Meal:
    '''
    Attributes:
        food: str
        price: float
        ingredients: list
    '''
def __init__(self):
    '''Creates the meal object'''
    self.food = ''
    self.price = 0
    self.ingredients = []

def set_food_name(self):
    '''Gives the meal object a price based on ingredients used in the meal'''
    self.food = input("What is the name of this meal?: ")
    return self.food

def set_price(self):
    '''sets the price of the meals'''
    for i in len(self.ingredients):
        self.price += self.ingredients[i].ingredient_price
    return self.price

def add_ingredients(self, ingredient):
    '''adds the ingredient to a list that makes up the meal'''
    self.ingredients.append(ingredient)

def remove_ingredients(self, ingredient):
    '''removes the last ingredient from the meal '''
    self.ingredients.pop()

def list_ingredients(self):
    '''displays a list of ingredients of the meal object'''
    for i in range(len(self.ingredients)):
        print(f'- {self.ingredients[1]}')