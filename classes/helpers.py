import re

def validate_input(correct_type, question, regex=r"", valids=[]):
    '''
    Prompts the user for a valid input. Default is casting user input into valid type\n
    correct_type: a value representing the target input type(if you want a float-> 0.0, int -> 1 etc...)\n
    question: The prompt for user input\n
    (optional)regex: Raw string regular expression if looking for specifically formatted user string(Like for dates MM-DD-YYYY)
    (optional)valids: A list containing valid items. First, input will be cast, then compared to list
    '''
    validated = False

    while not validated:
        user_input = input(question)
        cast = type(correct_type)

        # Checks for proper string formatting is regex provided
        if regex != "":
            if re.search(regex, user_input):
                validated = True
                user_input = re.findall(regex, user_input)
                continue
            else:
                print("Invalid input")
                continue
                
        # Ensures user input is of proper type
        if(type(user_input) != type(correct_type)):
            try:
                user_input = cast(user_input)
                if len(valids) == 0:
                    validated =True
                    continue  
            except ValueError:
                print("Invalid input, try again")
                validated = False
                continue

        # Checks for validity of input based on list of valid inputs provided
        if len(valids) != 0:
            if user_input in valids:
                validated = True
                continue
            else:
                print("Invalid input, try again")

    return user_input