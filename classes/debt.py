from datetime import datetime as dt
from datetime import timedelta as td
import json
import re
import helpers as help

VALID_INTERVALS = ["Monthly", "Yearly", "Biweekly", "Weekly"]
class Debt:
    '''
    Class used to represent user debts
    '''
    DEBT_COUNT = 0

    def __init__(self, debt_name = f"Debt {DEBT_COUNT}", start_amt = 0.0 ,curr_amt = 0.0, interest = 0.0, is_compound = True, interval = "MONTHLY"):
        '''
        Instantiates a Debt. Attributes of debt class:\n
        name (str)        -- The name given to debt for identification\n
        prin_amt (float)  -- The principal amount of debt\n
        amount (float)    -- The amount of debt currently owed\n
        interest (float)  -- The amount of interest being charged onto the debt. As a decimal\n
        is_compound (bool)-- States whether interest is principal or compount\n
        int_period (str)  -- The period that determines when interest is applied (monthly, yearly, etc.)\n
        start_date (date) -- The date when debt started to be tracked. Used for reporting purposes\n
        last_inc (date)   -- Date of last time interest was applied
        '''
        self.name = debt_name
        self.prin_amt = start_amt
        self.amount = curr_amt
        self.interest = interest
        self.is_compound = is_compound
        self.int_period = interval
        self.start_date = dt.now()
        self.last_inc = dt.now()
        self.DEBT_COUNT += 1

    def set_interest(self, new_interest):
        '''Sets interest of debt instance'''
        self.interest = new_interest
    
    def get_amount(self):
        '''Returns the amount of remaining debt left to pay'''
        return self.amount
    
    def get_interest(self):
        ''''''
        return self.interest

    def apply_interest(self):
        '''Increases debt amount by using interest defined'''
        self.amount += self.amount*self.interest
    
    def make_payment(self, payment):
        '''Reduces debt quantitiy by payment amount'''
        self.amount -= payment

    def estimate_debt(self, due_date, periodic_payment=0.0):
        '''Estimates the amount of debt after a given time period if 
        payment is made periodically before interest is applied'''
        
    def __str__(self):
        '''Returns description of debt's attributes'''
        int_type = ""
        if(self.is_compound):
            int_type = "Compound"
        else:
            int_type = "Principal"

        info = f"""'{self.name}' debt: \n
        Current debt is ${self.amount} at {self.interest*100}% interest applied {self.int_period} as {int_type} interest.\n
        Principal Debt quantity was ${self.prin_amt}, debt tracking was started on {self.start_date.strftime("%x")}
        """
        x = r"%x"
        info = f'~|Debt Name      |Initial     |Current     |Rate |Rate type |Applied  |Track Start    |Last Increment|~\n||{self.name: ^15}|{self.prin_amt: ^12}|{self.amount: ^12}|{self.interest: ^5}|{int_type: ^10}|{self.int_period: ^9}|{self.start_date.strftime(x): ^15}|{self.last_inc.strftime(x): ^14}||'
        return info
    
    def to_json(self):
        '''
        Returns Debt object in json string representation 
        '''
        # Objects attributes stored in dictionary
        start = self.start_date
        last = self.last_inc
        attr_dict = {
            "name": self.name,
            "amount": self.amount,
            "interest": self.amount,
            "is_compound": self.is_compound,
            "int_period": self.int_period,
            "start_date": [start.strftime("%Y"), start.strftime("%m"), start.strftime('%d')],
            "last_inc": [last.strftime("%Y"), last.strftime("%m"), last.strftime('%d')]
        }

        json_format = json.dumps(attr_dict, indent=4)
        return json_format

    @staticmethod
    def from_json(json_string):
        '''
        Creates a Debt instance based on given json string following format
        of to_json() method's json string
        '''
        attr_dict = json.loads(json_string)

        obj = Debt()

        obj.name = attr_dict["name"]
        obj.amount = attr_dict["amount"]
        obj.interest = attr_dict["interest"]
        obj.is_compound = attr_dict["is_compound"]
        obj.int_period = attr_dict["int_period"]

        start = attr_dict["start_date"]
        obj.start_date = dt.date(int(start[0]), int(start[1]), int(start[2]))

        last = attr_dict["last_inc"]
        obj.last_inc = dt.date(int(last[0]), int(last[1]), int(last[2]))

        return obj
    
    @staticmethod
    def create():
        '''
        Creates debt instance by prompting user for input
        '''
        name = input("Name your debt: ")
        amount = validate_input(0.0, "How much debt is owed?(ex. $12432.53, $200.0): $")
        interest = validate_input(0.0, "What is the debt's interest rate?(ex. For 12%, write 0.12): ")
        interval
        pass

def main():
#     thing = Debt()
#     x = thing.to_json() 
#     print(x)

#     y = '''{"name": "Debt 0","amount": 0,
#     "interest": 0,
#     "int_period": "Monthly",
#     "start_date": [
#         "2024",
#         "03",
#         "25"
#     ]
# }'''
#     other = Debt.from_json(y)
#     print(other)
    pass

main()