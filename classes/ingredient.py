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

    def get_calories(self):
        '''gets the calories of the ingredient'''
        valid = False
        while valid != True:
            try:
                self.calories = int(input())
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
        self.catagory = input("what nutritiona catagory is this item?: ").lower
    
    def __str__(self):
        


