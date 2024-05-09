import json
class Ingredients:
    
    '''
    Attributes:
        ingedient_name(str): Name of ingredient
        ingredient_price(float): Price of ingredient serving
        calories(int): Amount of calories in ingeredient serving
        nutrients(dict): mapping for amount of grams for 7 main categories of nutrients in a serving of ingredient 
    '''
    # Neccessary for retrieval purposes
    FOOD_GROUPS = ["Carbs", "Proteins", "Fats", "Vitamins", "Minerals", "Fibre"]
    def __init__(self):
        '''Creates the ingredient object'''
        self.ingredient_name = ''
        self.ingredient_price = 0
        self.calories = 0
        self.nutrients = {
            "Carbs": 0.0,
            "Proteins": 0.0,
            "Fats": 0.0,
            "Vitamins": 0.0,
            "Minerals": 0.0,
            "Fibre": 0.0
        }

    def __str__(self):
        cat_str = ""
        for category in self.nutrients:
            if(self.nutrients[category] != 0.0):
                cat_str += category + " "

        if len(cat_str) > 25:
            cat_str = cat_str[:20] + "..."

        info =  f"Ingredient: {self.ingredient_name}\nPrice: ${self.ingredient_price: .2f}\nCalories: {self.calories}\nCategories: {self.nutrients}"
        return f"~|{'Ingredient': ^12}|{'Price': ^9}|Calories |{'Nutrients': ^25} |~\n||{self.ingredient_name: ^12}|{self.ingredient_price: ^9}|{self.calories: ^9}|{cat_str: ^9}||"


    def set_calories(self):
        '''gets the calories of the ingredient'''
        valid = False
        while valid != True:
            try:
                self.calories = int(input("How many calories is the Ingredient: "))
                if self.calories < 0:
                    raise ValueError
                
            except ValueError:
                print("value must be an integer greater than 0")
            else:
                valid = True

    def set_ingredient_name(self):
        '''gets the name of the ingredient'''
        self.ingredient_name = input("Input the name of the ingredient: ")
        return self.ingredient_name

    def set_ingredient_price(self):
        '''gets the price of the ingredients'''
        valid = False
        while valid != True:
            try:
                self.ingredient_price = float(input("input the price of the ingredient: "))
                if self.ingredient_price < 0:
                    raise ValueError
            except ValueError:
                print("value must be an integer greater than 0")
            else:
                valid = True

    def set_ingredient_price(self):
        '''sets the price of the ingredients'''
        valid = False
        while valid != True:
            try:
                self.ingredient_price = float(input("input the price of the ingredient: "))
                if self.ingredient_price < 0:
                    raise ValueError
            except ValueError:
                print("value must be an integer greater than 0")
            else:
                valid = True

    def set_food_catagories(self):
        '''Sets ingredient categories'''
        categories = input("What nutritional category/categories does this item fall into?\nIf multiple, seperate by '.' (ex. grain.fruit): ")
        categories = categories.split(".")

        return self.category
    
    def to_json(self):
        attr_dict = {
            "ingredient_name": self.ingredient_name,
            "ingredient_price": self.ingredient_price,
            "calories": self.calories,
            "categories": self.nutrients
        }
        return json.dumps(attr_dict, indent=4)

    @staticmethod
    def from_json(json_string):
        '''
        Creates a static instance based on given json string following format
        of to_json() method's json string
        '''
        attr_dict = json.loads(json_string)
        
        obj = Ingredients()
        
        obj.ingredient_name = attr_dict["ingredient_name"]
        obj.ingredient_price = attr_dict["ingredient_price"]
        obj.calories = attr_dict["calories"]
        obj.nutrients = attr_dict["categories"]
        
        return obj
        
    
    @staticmethod
    def create():
        ingre = Ingredients()
        ingre.ingredient_name = ingre.set_ingredient_name()
        ingre.ingredient_price = ingre.set_ingredient_price()
        ingre.calories = ingre.set_calories()
        ingre.nutrients = ingre.set_food_catagories()
        return ingre

def main():
    #Create a subscription object
    ingredient = Ingredients.create()
    
    json_string = ingredient.to_json()
    print(json_string)
    print("\n")
    print(ingredient)
            
if __name__ == "__main__":
    main()