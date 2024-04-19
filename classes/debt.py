import datetime as dt

class Debt:
    '''
    Attributes of debt class:
    name (str)        -- The name given to debt for identification
    amount (float)    -- The amount of debt owed at a given time
    interest (float)  -- The amount of interest being charged onto the debt. As a decimal
    int_period (str)  -- The period that determines when interest is applied (monthly, yearly, etc.)
    start_date (date) -- The date when debt started to be tracked. Used for reporting purposes
    '''
    DEBT_COUNT = 0

    def __init__(self, debt_name = f"Debt {DEBT_COUNT}", amt = 0, interest = 0, interval = "Monthly"):
        self.name = debt_name
        self.amount = amt
        self.interest = interest
        self.int_period = interval
        self.start_date = dt.datetime.now()
        self.DEBT_COUNT += 1

    def set_interest(self, new_interest):
        '''Sets interest of debt instance'''
        self.interest = new_interest
    
    def get_amount(self):
        '''Returns the amount of remaining debt left to pay'''
        return self.amount
    
    def get_interes(self):
        ''''''
        return self.interest

    def apply_interest(self):
        '''Increases debt amount by using interest defined'''
        self.amount += self.amount*self.interest
    
    def make_payment(self, payment):
        '''Reduces debt quantitiy by payment amount'''
        self.amount -= payment

    def estimate_debt(self, due_date, periodic_payment=0.0):
        '''Estimates the amount of debt after a given time period if payment is made periodically before interest is applied'''
        


    def __str__(self):
        '''Returns description of debt's attributes'''
        info = f"""{self.name} debt: \n
        Current debt is {self.amount} at {self.interest*100}% interest applied {self.int_period}.\n
        Debt tracking was started on {self.start_date.strftime("%x")}
        """
        return info