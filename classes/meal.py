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
        info =  "Meal: " + self.food +"\nCost: "+ str(self.price) + "\nIngredients: "+ str(self.ingredients) 
        ing_list = ""
        for ingredient in self.ingredients:
            ing_list += ingredient + ", "
        ing_list = ing_list[:-2]
        if len(ing_list) >= 28:
            ing_list = ing_list[:28] + "..."

        return f"~|Meal     |Cost   |Ingredients                    |~\n||{self.food}|{self.price}|{ing_list: ^31}||\n"
    
    
    def to_json(self):
        attr_dict = {
            "Food name": self.food,
            "Meal price": self.price,
            "Ingredients": self.ingredients
        }
        return json.dumps(attr_dict)

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
    def from_json(json_string):
        '''
        Creates a static instance based on given json string
        following format of to_json() method's json string
        '''
        
        attr_dict = json.loads(json_string)
        
        obj = Meal()
        
        obj.food = attr_dict["Food Name"]
        obj.price = attr_dict["Meal Price"]
        obj.ingredients = attr_dict["Ingredients"]
        return obj
    
    @staticmethod
    def create():
        dood = Meal()
        dood.food = dood.set_food_name()
        dood.ingredients = dood.add_ingredients()
        dood.price = dood.set_price()
        return dood
    
    def edit_menu(self):
        menu_string = f"Editing Meals {self.name}\n\n1. Change name of meal\n2. add ingredients\n3. Change price of meal\n4. Back\nSelection: "
        while True:
            choice = help.validate_input(1, menu_string, valids=[1,2,3,4])
            if choice == 1:
                #Changing the Debt name
                self.food = input("Enter new meal name:")
            if choice == 2:
                self.ingredient = input(" Eneter new ingredient you  would  like to add   ")
            if choice == 3:
                self.price = help.validate_input(0.0, "Enter new of current meal:")
            if choice == 4:
                return 
            
def main():
    #Create a subscription object
    meal = Meal.create()
    x = Meal
    x.edit_menu
    
    json_string = meal.to_json()
    print(json_string)
    print("\n")
    print(meal)
            
if __name__ == "__main__":
    main()
