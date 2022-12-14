# Time for some spicy class/object associations!!! :)

# Code/Structure for bank account
class BankAccount:
    # ! Class Attribute
    bank_accounts = []
    # initializer/constructor for bank account
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts.append(self)
    def deposit(self, amount):
        # deposit the amount to the balance variable
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        # withdraw the amount from the balance variable
        if (self.balance < amount):
            print(f"Insufficient funds! Available balance is {self.balance}. Requested amount: {amount}")
        else:
            self.balance = self.balance - amount
        return self
    def display_account_info(self):
        # show all the information associated with the account
        print(f"The interest rate on is: {self.int_rate}")
        print(f"The available balance is: {self.balance}")
        return self
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def print_instances(cls):
        # we use cls to refer to the class
        for i in range(0, len(cls.bank_accounts)):
            print(cls.bank_accounts[i].int_rate)
            print(cls.bank_accounts[i].balance)

# code/structure for Users
class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.member = False
        self.gold_points = 0
        self.checkingAccount = BankAccount(.04,0)
        self.savingsAccount = BankAccount(.09,0)
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(f"is member: {self.member}")
        print(f"gold points balance: {self.gold_points}")
        print("showing savings account info:")
        self.savingsAccount.display_account_info()
        print("showing checking account info:")
        self.checkingAccount.display_account_info()
        return self
    
    def enroll(self): 
        if (self.member):
            print(f"{self.first_name} is already a member")
        else:
            self.member = True
            print(f"{self.first_name} is now a member. Welcome to the club! Help yourself to punch and pie.")
            self.gold_points = 200
            print(f"gold points balance is now: {self.gold_points}")
        return self
    
    def spend_points(self, amount):
        if amount <= self.gold_points:
            self.gold_points = self.gold_points - amount
            print(f"New gold points balance is {self.gold_points}")
        elif amount > self.gold_points:
            initial_points = self.gold_points
            new_amount = amount - self.gold_points
            self.gold_points = self.gold_points - amount
            print(f"Not enough points to cover purchase. Initial points balance: {initial_points}. Amount requested: {amount} Please pay {new_amount} point(s) to complete your purchase.")
        return self

    def make_savings_deposit(self, amount):
        self.savingsAccount.deposit(amount)
    def make_savings_withdrawal(self, amount):
        self.savingsAccount.withdraw(amount)
    def display_user_savings_balance(self):
        self.savingsAccount.display_account_info()
    
    def make_checking_deposit(self, amount):
        self.checkingAccount.deposit(amount)
    def make_checking_withdrawal(self, amount):
        self.checkingAccount.withdraw(amount)
    def display_user_checking_balance(self):
        self.checkingAccount.display_account_info()

    def transfer_money(self, amount, other_user):
        self.checkingAccount.withdraw(amount)
        other_user.checkingAccount.deposit(amount)


# ask why I can't chain the display_info methods to depost/withdraw methods
rick = User("Rick", "Sanchez", "rick@r&m.org", 70)
rick.display_info()
rick.make_savings_deposit(500)
rick.display_info()
rick.make_savings_withdrawal(100)

morty = User("Morty", "Smith", "morty@r&m.org", 14)

rick.checkingAccount.deposit(1000)
rick.transfer_money(50,morty)

morty.display_info()
rick.display_info()