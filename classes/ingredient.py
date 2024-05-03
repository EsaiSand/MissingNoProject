import json
class Ingredients:
    
    '''
    Attributes:
        ingedient_name: str
        ingredient_price: float
        calories: int
        categories: str
    '''
    
    def __init__(self):
        '''Creates the ingredient object'''
        self.ingredient_name = ''
        self.ingredient_price = 0
        self.calories = 0
        self.catagories = ''

    def __str__(self):
        return f"Ingredient: {self.ingredient_name}\nPrice: ${self.ingredient_price: .2f}\nCalories: {self.calories}\nCategories: {self.catagories}"

    def to_json(self):
        return json.dumps(self.__dict__)

    def get_calories(self):
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

        return self.calories

    def get_ingredient_name(self):
        '''gets the name of the ingredient'''
        self.ingredient_name = input("input the name of the ingredient: ")
        return self.ingredient_name


    def get_ingredient_price(self):
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

        return self.ingredient_price

    def get_food_catagories(self):
        self.catagory = input("what nutritional catagory is this item?: ")
        return self.catagory
        
    @staticmethod
    def create():
        ingre = Ingredients()
        ingre.ingredient_name = ingre.get_ingredient_name()
        ingre.ingredient_price = ingre.get_ingredient_price()
        ingre.calories = ingre.get_calories()
        ingre.catagories = ingre.get_food_catagories()
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