class BankAccount:

    def _init_(self, first_name, last_name,  bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))

    def withdraw(self, amount):
        if amount <= 0:
            print("You cannot withdraw zero or negative")
        elif amount > self.balance:
            print("You don't have enough balance")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))


    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)
    
    def give_loan(self,loan):
        if loan <=0:
            print("amount is too low")
        else:
            self.balance += loan
            print("You have requested  {} ".format(loan))

      
    def withdrawal_statement(self):
        withdrawal=withdrawal.append(withdraw())
        return withdraw

    def loan_repay(self,amount):
        if amount >=1:
            self.repay=self.loans-amount
            print("You have repayed Ugsh {}".format(amount))
            print("Your loan balance is: {}".format(self.repay))