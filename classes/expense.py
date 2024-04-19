class Expense:
    '''A class to represent an expense with various attributes.
    
    Attributes:
        name (str): The name of the expense.
        cost (float): The cost of the expense.
        date (str): The date of the expense in YYYY-MM-DD format.
        category (str): The category of the expense.
        categories (list): A list of possible expense categories.
    '''
    
    def __init__(self):
        '''Initialize an Expense object with default values.'''
        self.name = ''
        self.cost = 0.0
        self.date = ''
        self.category = ''
        self.categories = []

    def set_name(self, name: str):
        '''Set the name of the expense.
        
        Args:
            name (str): The name of the expense.
        '''
        self.name = name

    def set_cost(self, cost: float):
        '''Set the cost of the expense.
        
        Args:
            cost (float): The cost of the expense.
        '''
        self.cost = cost

    def set_date(self, date: str):
        '''Set the date of the expense.
        
        Args:
            date (str): The date of the expense in YYYY-MM-DD format.
        '''
        self.date = date

    def set_category(self, category: str):
        '''Set the category of the expense.
        
        Args:
            category (str): The category of the expense.
        '''
        if category in self.categories:
            self.category = category
        else:
            print(f"Error: '{category}' is not a valid category. Please add it first.")

    def add_category(self, category: str):
        '''Add a new category to the list of categories.
        
        Args:
            category (str): The new category to add.
        '''
        if category not in self.categories:
            self.categories.append(category)
            print(f"Category '{category}' added.")
        else:
            print(f"Category '{category}' already exists.")

    def remove_category(self, category: str):
        '''Remove a category from the list of categories.
        
        Args:
            category (str): The category to remove.
        '''
        if category in self.categories:
            self.categories.remove(category)
            print(f"Category '{category}' removed.")
        else:
            print(f"Error: '{category}' does not exist.")

def main():
    # Create an Expense object
    expense = Expense()
    
    # Menu loop
    while True:
        print("\nOptions:")
        print("1. Add a category")
        print("2. Remove a category")
        print("3. Set expense name")
        print("4. Set expense cost")
        print("5. Set expense date")
        print("6. Set expense category")
        print("7. View expense details")
        print("8. Exit")

        choice = input("\nChoose an option (1-8): ")

        if choice == "1":
            # Add a category
            category = input("\nEnter the category name: ")
            expense.add_category(category)

        elif choice == "2":
            # Remove a category
            category = input("\nEnter the category name to remove: ")
            expense.remove_category(category)

        elif choice == "3":
            # Set expense name
            name = input("\nEnter the expense name: ")
            expense.set_name(name)
            print(f"Expense Name: {expense.name}")

        elif choice == "4":
            # Set expense cost
            while True:
                try:
                    cost = float(input("\nEnter the expense cost: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            expense.set_cost(cost)
            print(f"Expense Cost: ${expense.cost:.2f}")

        elif choice == "5":
            # Set expense date
            date = input("\nEnter the expense date (YYYY-MM-DD): ")
            expense.set_date(date)
            print(f"Expense Date: {expense.date}")

        elif choice == "6":
            # Set expense category
            category = input("\nEnter the category for the expense: ")
            expense.set_category(category)
            if expense.category:
                print(f"Expense Category: {expense.category}")

        elif choice == "7":
            # View expense details
            print("\nExpense Details:")
            print(f"Name: {expense.name}")
            print(f"Cost: ${expense.cost:.2f}")
            print(f"Date: {expense.date}")
            print(f"Category: {expense.category}")

        elif choice == "8":
            # Exit the program
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
