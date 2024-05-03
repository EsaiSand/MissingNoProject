import json
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
            
    def __str__(self) -> str:
        return "Meal: " + self.food +"\nCost: "+ str(self.price) + "\nIngredients: "+ str(self.ingredients) 
    
    
    def to_json(self):
        return json.dumps(self.__dict__)

    def set_food_name(self):
        '''Gives the meal object a price based on ingredients used in the meal'''
        self.food = input("What is the name of this meal?: ")
        return self.food

    def set_price(self):
        '''sets the price of the meals'''
        for i in len(self.ingredients):
            self.price += self.ingredients[i].ingredient_price
        return self.price

    def add_ingredients(self):
        '''adds the ingredient to a list that makes up the meal'''
        valid = False
        while valid != True:
            ingredient = input("What ingredient would you like to add   ")
            self.ingredients.append(ingredient)
            response = input("Would you like to add another ingredient (Y/N) ?  ")
            if response == "Y"or response == "y":
                continue
            else:
                valid = True
            
        self.ingredients.append(ingredient)

    def remove_ingredients(self, ingredient):
        '''removes the last ingredient from the meal '''
        self.ingredients.pop()

    def list_ingredients(self):
        '''displays a list of ingredients of the meal object'''
        for i in range(len(self.ingredients)):
            print(f'- {self.ingredients[1]}')
            
    @staticmethod
    def create():
        dood = Meal()
        dood.food = dood.set_food_name()
        dood.ingredients = dood.add_ingredients()
        dood.price = dood.set_price()
        return dood
        
    
def main():
    #Create a subscription object
    meal = Meal.create()
    
    
    json_string = meal.to_json()
    print(json_string)
    print("\n")
    print(meal)
            
if __name__ == "__main__":
    main()