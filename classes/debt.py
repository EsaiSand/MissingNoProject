import datetime as dt
from datetime import timedelta as td
from dateutil.relativedelta import relativedelta  
import json
import re
import helpers as help



class Debt:
    '''
    Class used to represent user debts
    '''
    DEBT_COUNT = 0
    VALID_INTERVALS = ["Yearly", "Monthly", "Biweekly", "Weekly"]
    INTERVAL_DELTAS = {
        "Monthly": relativedelta(months=1),
        "Yearly": relativedelta(years=1),
        "Biweekly": relativedelta(weeks=2),
        "Weekly": relativedelta(weeks=1)
    }

    def __init__(self):
        '''
        Instantiates a Debt. Attributes of debt class:\n
        name (str)        -- The name given to debt for identification\n
        prin_amt (float)  -- The principal amount of debt\n
        amount (float)    -- The amount of debt currently owed\n
        interest (float)  -- The amount of interest being charged onto the debt. As a decimal\n
        is_compound (bool)-- States whether interest is principal or compount\d\n
        int_period (str)  -- The period that determines when interest is applied (monthly, yearly, etc.)\n
        start_date (date) -- The date when debt started to be tracked. Used for reporting purposes\n
        last_inc (date)   -- Date of last time interest was applied
        '''
        self.name = f"Debt {0}"
        self.prin_amt = 0.0
        self.amount = 0.0
        self.interest = 0.0
        self.is_compound = True
        self.int_period = "Monthly"
        self.start_date = dt.datetime.now()
        self.last_inc = dt.datetime.now()
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

    def update_debt(self):
        '''Updates debt amount by applying corresponding interest since last time
        it was applied'''
        # Holds value of next date interest should be applied after 
        next_date = self.last_inc + Debt.INTERVAL_DELTAS[self.int_period]

        # Increases debt while "next" interest date has already passed
        while(next_date < dt.datetime.now()):
            self.amount += self.amount*self.interest
            self.last_inc = next_date
            next_date += Debt.INTERVAL_DELTAS[self.int_period]
    
    def make_payment(self, payment):
        '''Reduces debt quantitiy by payment amount'''
        self.amount -= payment

    def estimate_debt(self, due_date, periodic_payment=0.0):
        '''Estimates the amount of debt after a given time period if 
        payment is made periodically before interest is applied'''
        estimate = self.amount
        next_date = self.last_inc + Debt.INTERVAL_DELTAS[self.int_period]

        while(next_date < due_date):
            estimate += estimate*self.interest
            next_date += Debt.INTERVAL_DELTAS[self.int_period]

        return estimate
        
    def __str__(self):
        '''Returns description of debt's attributes'''
        int_type = ""
        if(self.is_compound):
            int_type = "Compound"
        else:
            int_type = "Principal"

        # info = f"""'{self.name}' debt: \n
        # Current debt is ${self.amount} at {self.interest*100}% interest applied {self.int_period} as {int_type} interest.\n
        # Principal Debt quantity was ${self.prin_amt}, debt tracking was started on {self.start_date.strftime("%x")}
        # """
        x = r"%x"
        info = f'~|Debt           |Initial     |Current     |Rate |Rate type |Applied  |Track Start    |Last Increment|~\n||{self.name: ^15}|{self.prin_amt: ^12}|{self.amount: ^12}|{self.interest: ^5}|{int_type: ^10}|{self.int_period: ^9}|{self.start_date.strftime(x): ^15}|{self.last_inc.strftime(x): ^14}||'
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

        new_debt = Debt()

        new_debt.name = attr_dict["name"]
        new_debt.amount = attr_dict["amount"]
        new_debt.interest = attr_dict["interest"]
        new_debt.is_compound = attr_dict["is_compound"]
        new_debt.int_period = attr_dict["int_period"]

        start = attr_dict["start_date"]
        new_debt.start_date = dt.datetime.date(int(start[0]), int(start[1]), int(start[2]))

        last = attr_dict["last_inc"]
        new_debt.last_inc = dt.datetime.date(int(last[0]), int(last[1]), int(last[2]))

        return new_debt
    
    @staticmethod
    def create():
        '''
        Creates debt instance by prompting user for input
        '''
        int_types = {"Compound": True, "Principal": False}
        new_debt = Debt()

        new_debt.name = input("Name your debt: ")
        new_debt.prin_amt = help.validate_input(0.0, "What was the initial loan for the debt?(ex. $12432.53, $200.0): $")
        new_debt.amount = help.validate_input(0.0, "How much debt is currently owed?(ex. $12432.53, $200.0): $")
        new_debt.interest = help.validate_input(0.0, "What is the debt's interest rate?(ex. For 12%, write 0.12): ", regex=r"(^(0\.[0-9][0-9])|(1\.[0-9][0-9]))")
        new_debt.is_compound = int_types[help.validate_input("d", "What type of interest is it?(Compound or Principal): ", valids=["Compound", "Principal"])]
        new_debt.int_period = Debt.VALID_INTERVALS[help.validate_input(1, "Select the debt's interest period:\n1. Yearly\n2. Monthly\n3. Biweekly\n4. Weekly\nSelection: ", valids=[1,2,3,4])-1]
        last_inc_str = help.validate_input(" ", "When was interest last applied?(Use MM-DD-YYYY format): ", regex=r"(^(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])-((20(([01][0-9])|(2[0-4])))|(19[0-9][0-9])))")[0][0]

        print(last_inc_str)
        mark = last_inc_str.find("-")
        month = int(last_inc_str[0:mark])
        last_inc_str = last_inc_str[mark+1:]
        mark = last_inc_str.find("-")
        day = int(last_inc_str[0:mark])
        year = int(last_inc_str[mark+1:])
        date = dt.datetime(year, month, day)

        new_debt.last_inc = date

        print(f"Created new debt:\n{str(new_debt)}")
        return new_debt

def main():
    # x = relativedelta(months=1)
    # print(x)

    debt = Debt()
    debt.last_inc -= Debt.INTERVAL_DELTAS["Monthly"]
    print(debt)
    debt.update_debt()
    print(debt)

    # Debt.create()

main()