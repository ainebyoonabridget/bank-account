class account:
    
    def __init__(self,first_name,last_name,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance =0
        self.phone_number=phone_number
        self.bank=bank
        self.deposit=deposit[]
        self.withdraw=withdraw[]

        def get_currentTime(self);
        now=datetime.now()
        time_formatted=now.strftime("%b %d %Y,%H %M %S")
        return time_formatteds

    def get_loan(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount<=0:
            print("A loan cannot be offered at the moment")
            else:
                if self.loan=amount
                print("You have sucessfully recieved a loan of {}".format(amount))
    
    def account_name(self):
        name ="account for {} {}".format(self.first_name,self.last_name)
        return name
    
    def  deposit(self,amount):
        try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

        if amount =0:
            print("You cannot deposit a negative amount")
        else:
            self.balance +=amount
            self.deposit.append(deposit)  
            time=date.time()
            deposit={
                "time":time,
                "amount":amount
            }
            formated_time=time.strftime{"%m %drd %Y, %H;%M:%S" }
            print("You have deposited {} on {} ".format(amount,self.account,formated_time))
      

    def get_balance(self):
        return "{} balance is {} ".format(self.account_name(),self.balance)

    def withdraw(self,amount):
         try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

      if amount=0:
      print("You cannot withdraw zero amount")
      elif amount >self.balance:
          print("You dont have enough balance to make this request")
      else:
          self.balance>=amount
          self.withdraw.append(amount)   
           formated_time=stime.strftime{"%m %drd %Y, %H;%M:%S"}
          print("You have withdrawn {} from {}".format (self.account_name,self.amount,formated_time))

    def deposit_statement(self):
      for deposit in self.deposit:
          time=diposit['time']
          formated_time=time.strftime{"%m %drd %Y, %H;%M:%S"}
          amount=deposit["amount"]
          statement="You have deposited {} on {}. Your new balance is {}".format(self.amount,formated_time,self.balance)
          print(statement)
     


def  withdraw_statement(self,amount):
   for withdraw in self.withdrawa:
       time=deposit["time"]
       formated_time=time.strftime{"%m %drd %Y, %H:%M:%S"}
       amount withdraw=["amount"]
       statement="You have sucessfully withdrawn {} on {}".format(amount,formated_time)
       print (statement)

def pay_loan(self,amount):
     try:
            amount +1
            expect TypeError:
            print ("You can only enter a digit value")
            return

    if amount>=0:
    print(" You have insufficient balance to repay the loan")
    
    elif self.loan==0:
            print("You don't have a loan at this moment")
     
    elif amount> self.loan:
             print("Your loan is {}, an amount less or equal is required".format(self.loan))
    else:self.loan-=amount
    time=datetime.now()  
    payment={
        "time":time,
        "amount":amount
    }   
    self.pay_loan.append(payment)   
    print("You have repaid your loan with {}. Your loan balance is {}".format(amount,self.loan))

    def pay_loan_statement(self):
        for payment in self.pay_loan:
        time=payment('time')
        amount=payment[amount]
        formated_time=self.get_formated_time(time)
        statement=("You have repaid{} on{}".format( amount,formated_timess))


class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_number,bank);
    self.bank=bank
    super().__init__(first_name,last_name,phone_number)


class MobileMoneyAccount(account):
 def__init__(self,first_name,last_name,phone_number,service_provider):
    self.service_provider= service_provider
    self.airtime=[]
    self.pay_bills=[]
    self.send_money=[]
    self.recieve_money[]
    
    super().__init__(first_name,last_name,phone_number)

def  buy_airtime(self,amount);
    try:
       amount+1
    expect TypeError:
        print("Please enter the amount in digits")
    return

   if amount>self.balance:
       print("Yello, You have insufficient balance to make this request")
  else:
      self.balance<=amount
      time=datetime.now() 
      airtime={
          "time":time,
          "airtime":amount
      }    
      self.airtime.append(airtime)
      print("You have bought airtime worth{} on {}".format (amount,self.get_formated_time(time)))

 def pay_bills(self,amount):
        try:
            amount+1
        expect TypeError:
            print("Please enter the amount in figures")
            return
    
    if amount>self.balance:
        print("You have insufficient balance to make this request")
    else:
        self.balance<=amount
        time=datetime.now()   
        pay_bills{
            "time":time,
            "pay_bills":amount
        }
        self.pay_bills.append(pay_bills)
        print("You have successfully paid your bills worth {} on {}".format (amount,get_formated_time(time)))


def send_money(self,amount):
    try:
        amount+1
        expect TypeError:
        print("Enter the amount in figures")
        return

        if amount>self.balance:
            print("You have insufficient balance to make the transaction")

        else:
            self.balance>=amount
            time=datetime.now()
            send_money{
                "time":time,
                "send_money":amount
            }
            self.send_money.append(send_money)
            print("You have successfully transfered  money {} from your account on {}. Your new balance is {}".format (amount,get_formated_time(time),self.balance))


def recieve_money(self,amount):
    time=datetime.now()
    recieve_money{
        "time":time,
        "recieve_money":amount
    }
    self.recieve_money.append(recieve_money)
    print("You have recieved {} on {} your new balance is {}".format(amount,get_formated_time(time),self.balance)) 

           