import datetime as dt

class Debt:
    def __init__(self, debt_name, amt, interest):
        self.name = debt_name
        self.amount = amt
        self.interest = interest                       # As decimal (5% = 0.05)
        self.start_date = dt.datetime.now()

    def set_interest(self, new_interest):
        self.interest = new_interest
    
    def get_amount(self):
        return self.amount
    
    def get_interes(self):
        return self.interest

    def to_string(self):
        info = f"""{self.name} debt: \n
        Current debt is {self.amount} at {self.interest*100}% interest\n
        Debt tracking was started on {self.start_date.strftime("%x")}
        """
        return info
    
    def make_payment(self, payment):
        self.amount -= payment