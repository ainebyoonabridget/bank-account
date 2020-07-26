from datetime import datetime
time = datetime.now()
print(time)
class BankAccount:
    def __init__(self, first_name, last_name, Phone_nnumber, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.Phone_number = Phone_number
        self.bank = bank
        self.withdrawals = []
        self.deposits =[]
        self.balance = 0
        self.loan = 0

    def account_name(self):
        name = "{}  account for {} {}".format(self.bank, self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")

        else:
            self.balance += amount
            self.deposits.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("You have deposited {} to {} on {}".format(amount, self.account_name(), formated_time))
            return
    def withdraw(self, amount):
        try:
            amoount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative amount")

        elif amount > self.balance:
            print("You have insufficient balance to withdraw this amount")

        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
     return "The balance for {} is {}".format(self.account_name(), self.balance)

    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))

    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            print(withdraw)

    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot request for an amount less than zero")
        else:
             self.loan = amount
             print("You have been given a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("Too low to repay your amount")
        elif self.loan == 0:
            print("You don't have a loan at this moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            print("You have repaid your loan with {} your balance is {}".format(amount, self.loan))


acc1 = BankAccount("Ainebyoona", "Bridget", +256779369759, "Centenary")
acc1.first_name
acc1.deposit(1000)
print(acc1.first_name)
acc1.deposit(5302)
print(acc1.balance)
acc1.request_loan(3000)
acc1.repay_loan(100)
acc1.repay_loan(24798)
acc1.repay_loan(3000)
print(acc1.loan)
print(acc1.balance)
acc1.request_loan(258579)
acc1.deposit(500)
acc1.deposit("twenty")
acc1.deposit(9040)
acc1.deposit(8368)
acc1.show_deposit_statements()
acc1.request_loan("thirty") 

           