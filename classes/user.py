class User:
    '''
    Attributes:
        name: str
        email: str
        password: str
        income: float
        funds: float
        pay_Schedule: int
    '''
def __init__(self, name = "user", email = "", password = "password", income = 0.0, funds = 0.0, schedule = 0):
    '''Creates the user object with default attributes if none provided'''
    self.name = name
    self.email = email
    self.password = password
    self.income = income
    self.funds = funds
    self.pay_schedule = schedule

def set_username(self, username):
    '''Sets the username of the user'''
    self.name = username

def set_password(self, password):
    '''Sets the password of the user'''

def set_email(self, email):
    '''Sets the email of the user'''

def set_income(self, income):
    '''Sets the income of the user'''

def set_pay_schedule(self, new_sched):
    '''Sets the payment schedule'''

def get_funds(self, funds):
    '''Gets the ammount of funds that the user has available'''

def __str__(self):
    '''To string method for user class'''
    info = f"""USER {self.name}:
        Email: {self.email}
        Password: {self.password}
        Income: {self.income}
        Funds: {self.funds}
        Pay Schedule: {self.pay_schedule}"""
    return info