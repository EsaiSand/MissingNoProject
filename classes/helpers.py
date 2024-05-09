import re
from datetime import datetime as dt

def validate_input(correct_type, question, regex=r"", valids=[], pos=True):
    '''
    Prompts the user for a valid input. Default is casting user input into valid type\n
    correct_type: a value representing the target input type(if you want a float-> 0.0, int -> 1 etc...)\n
    question: The prompt for user input\n
    (optional)regex: Raw string regular expression if looking for specifically formatted user string
    (optional)valids: A list containing valid items. First, input will be casted, then compared to list
    (optional)pos: Used for when casting to number. Denotes if input should be positive
    '''
    validated = False
    while not validated:
        user_input = input(question)
        cast = type(correct_type)

        # Checks for proper string formatting if regex provided
        if regex != "":
            if re.search(regex, user_input):
                validated = True
                print(re.findall(regex, user_input))
                user_input = re.findall(regex, user_input)[0]
                
                if type(correct_type) == type("string"):
                    continue
            else:
                print("Invalid input, try again\n")
                continue
                
        # Ensures user input is of proper type
        if(type(user_input) != type(correct_type)):
            try:
                user_input = cast(user_input)

                # If cast was to number, validate if negatives allowed based on pos
                if (cast == type(1) or cast == type(1.0)) and pos == True:
                    validated = user_input >= 0 
                # If we have a list of valids to check against, not done yet
                if len(valids) == 0:
                    validated = True
                else:
                    validated = False

            except ValueError:
                print("Invalid input, try again\n")
                validated = False
                continue

        # Checks for validity of input based on list of valid inputs provided
        if len(valids) != 0:
            if user_input in valids:
                validated = True
            else:
                print("Invalid input, try again\n")
                
    return user_input


def validate_date(question, max_date=dt.today(), min_date=dt(1900,1,1)):
    '''
    Prompts user for valid date following MM-DD-YYYY format

    question: Prompt for user input
    max_date(opt): Date object representing max user input date. Defaults to current day
    min_date(opt): Date object representing minimum user input date. Defaults to Jan 1, 1900
    '''
    # Regular Expression for dates with format MM-DD-YYYY
    regex=r"(^(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])-[0-9]{4})"
    validated = False

    while not validated:
        user_input = input(question)

        # Checks if input follows MM-DD-YYYY format
        if re.search(regex, user_input):
            user_input = re.findall(regex, user_input)[0][0]

            # Parsing year, month, day from input
            mark = user_input.find("-")
            month = int(user_input[0:mark])
            user_input = user_input[mark+1:]
            mark = user_input.find("-")
            day = int(user_input[0:mark])
            year = int(user_input[mark+1:])

            # Attempts to create valid date from input
            try:
                date = dt(year, month, day)
                user_input = date
            except ValueError:
                print("Invalid date: This date does not exist, try again\n")

            # Checks that date is within bounds
            if date > max_date:
                print(f"Invalid date: Pick a date before {max_date.strftime(r'%x')}\n")
            elif date < min_date:
                print(f"Invalid date: Pick a date after {min_date.strftime(r'%x')}\n")
            else:
                validated = True
            

            continue
        else:
            print("Invalid input, try again\n")
            continue
    
    return user_input

def main():
    print(type('x'*20))

if __name__ == "__main__":
    main()