class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Your deposit of {self.amount} was successfully credited to your account. \nYour new balance = {self.balance}")
    
    def withdraw(self,with_amt):
        self.with_amt = with_amt
        self.balance -= self.with_amt
       
        if self.balance >= self.with_amt:
            print(f"{self.with_amt} was withdrawn from your account. \nYour new balance = {self.balance}")
        else: 
            return "Insufficient balance"
    def __str__(self):
        return f"Name: {self.owner} \nCurrent Balance: {self.balance}"
