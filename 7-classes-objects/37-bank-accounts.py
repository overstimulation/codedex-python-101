class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def display_balance(self):
        print(f'The current balance is {self.balance}')

my_account = BankAccount('Kacper', 'Bednarczuk', 333, 'Personal', 1234, 7000.0)
my_account.deposit(96)
my_account.withdraw(25)
my_account.display_balance()