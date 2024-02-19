class bank:
    def __init__(self,bankaccount,bank_name):
        self.balance=bankaccount
        self.name=bank_name
        print(f"\n{self.name}:{self.balance} account created")
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"hello'{self.name},deposited{self.balance}")
    def withdraws(self,withdraw):
        self.balance=self.balance-withdraw
        print(f"hello successfully withdrawn{withdraw}from your account\nbalance:{self.balance}")
    def saving(self,amount,intention):
        self.balance=self.balance-amount
        self.save=amount
        print(f"you have saved,{amount} for,{intention},balance:{self.balance}")
   
    def intrests(self):
        if self.save<500:
            intrest=1/100
            self.balance=self.balance*intrest+self.balance
            print(f"your money will grow for an amount of{self.balance}")
        else:
       
            intrest=2/100
            self.balance=self.balance*intrest+self.balance
            print(f"your money will grow for an amount of{self.balance}")
        
    def send(self,sending):
        if sending>self.balance:
            print(f"sending failed balance of:{self.balance}")
        else:
            self.balance=self.balance-sending
            print(f"{sending},has been sent")