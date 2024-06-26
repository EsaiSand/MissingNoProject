import json
import helpers as help
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
        self.name = ''
        self.price = 0
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

        cat_str = cat_str[:-1]

        return f"~|{'Ingredient': ^12}|{'Price': ^9}|Calories |{'Nutrients': ^45}|~\n||{self.name: ^12}|{self.price: ^9}|{self.calories: ^9}|{cat_str: ^45}||\n"
    
    def to_json(self):
        attr_dict = {
            "ingredient_name": self.name,
            "ingredient_price": self.price,
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
        
        obj.name = attr_dict["ingredient_name"]
        obj.price = attr_dict["ingredient_price"]
        obj.calories = attr_dict["calories"]
        obj.nutrients = attr_dict["categories"]
        
        return obj
        
    @staticmethod
    def create():
        ingre = Ingredients()
        ingre.name = input("Name of ingredient: ")
        ingre.price = help.validate_input(0.0, f"What is the cost of a serving of {ingre.name}?: $", pos=True)
        ingre.calories = help.validate_input(1, f"How many calories in a serving of {ingre.name}?: ", pos=True)
        for categroy in ingre.nutrients:
            ingre.nutrients[categroy] = help.validate_input(0.0, f"How many grams of {categroy} does a serving of {ingre.name} have?: ")

        return ingre

    def edit_menu(self):
        menu_string = f"Editing Ingredient {self.name}\n\n1. Change name\n2. Change price for serving\n3. Change calorie count per serving\n4. Edit nutrients\n5. Back\nSelection: "
        
        while True:
            choice = help.validate_input(1, menu_string, valids=[1,2,3,4])

            if choice == 1:
                # Changing Name
                self.name = input("Enter new name: ")
            if choice == 2:
                self.price = help.validate_input(0.0, "Enter new price per serving: ")
            if choice == 3:
                self.calories = help.validate_input(1, "Enter new calorie count per serving")
            if choice == 4:
                for categroy in self.nutrients:
                    self.nutrients[categroy] = help.validate_input(0.0, f"How many grams of {categroy} does a serving of {self.name} have?: ")
            if choice == 5:
                return

def main():
    #Create a subscription object
    x = Ingredients()

    x.edit_menu()
            
if __name__ == "__main__":
    main()