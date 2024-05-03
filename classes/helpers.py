import re

def validate_input(correct_type, question, regex=r"", valids=[]):
    '''
    Prompts the user for a valid input. Default is casting user input into valid type\n
    correct_type: a value representing the target input type\n
    question: The prompt for user input\n
    (optional)regex: Raw string regular expression if looking for specifically formatted user string, or number ranges
    '''
    user_input = input(question)
    cast = type(correct_type)
    validated = False

    while not validated:
        # Ensures user input is of proper type
        while(type(user_input) != type(correct_type)):
            try:
                user_input = cast(user_input)
                validated = True  
            except ValueError:
                print("Invalid input, try again")
                validated = False
                user_input = input(question)

        # Checks for proper string formatting is regex provided
        if regex != "":
            if not re.search(regex, user_input):
                validated = False

        # Checks for validity of input based on list of valid inputs provided
        if valids.length() != 0:
            if user_input not in valids:
                validated = False

    return user_input