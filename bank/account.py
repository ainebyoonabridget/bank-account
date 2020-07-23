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
    
    def give_loan(self,loan):
        if loan <=0:
            print("amount is too low")
        else:
            self.balance += loan
            print("You have requested  {} ".format(loan))

    def deposit (self, amount):
        if amount <=0:
            print("You can not deposit zero or negative")
        else:
            self.balance +=amount
            self.deposits.append(amount)
            print("You have deposited {}".format(amount,self.account_name()))

    def withdrawal(self,amount):
        if withdrawal<=0:
            print("You can not withdraw zero or negative")
        elif amount > self.balance:
            print("You dont have enough balance")
        else:
            self.balance=amount
            self.withdrawal.append(amount)
            print("You have withdrawn {} from {}".format(amount,self.account_name()))
    
    def get__balance(self):
        return("The balance for {}".format(self.account_name(), self.balance))

    def show_deposit_statement(self):
        for deposits in self.deposits:
            print(deposit)

    def request_loan(self, amount):
            if amount<=0:
                print("You can not requesta loan at this moment")
            else:
                self.loan=amount
                print("You have been given a loan of {}".format(amount))

    def repay_loan(self,amount):
        if amount <=0:
            print("You cannot repay with that amount")
        elif self.loan==0:
            print("You dont have a loan at this moment")
        elif amount=self.loan:
            print("Your loan is {}. Please an amount less or equal".format(self.loan))
        else:
            self.loan==amount
            print("You haverepaid yourloan with {}. Your loan balanceis {}".format(amount,self.loan))

           