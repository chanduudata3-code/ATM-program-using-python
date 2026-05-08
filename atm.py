class ATM:
    def __init__(self,pin,balance,limit):
        self.pin = pin
        self.balance = balance
        self.limit = limit
        
    def Menu(self):
        print("Welcome to ATM")
        print("1.Check Bank Balance\n2.Withdraw\n3.Deposit\n4.Exit")
        while 1:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.CheckBalance()
            elif ch == 2:
                self.Withdraw()
            elif ch == 3:
                self.deposit()
            elif ch == 4:
                self.Exit()
                break
            

    def Check_pin(self):
        while self.limit != 0:
            pin = int(input("Enter your pin: "))
            if self.pin == pin:
                self.Menu()
                break
            else:
                print("invalid pin")
            self.limit -= 1
        if self.limit == 0:
            print("Account Blocked")
            
        
    def CheckBalance(self):
        if self.balance == 0:
            print("You have Zero Balance")
        else:
            print("Your Balance is:",self.balance)
            
    def Withdraw(self):
        amt = int(input("Enter amount to withdraw:"))
        if amt < 20000:
            
            
            if (self.balance - amt) > 500: 
                if self.balance < amt:
                    print("Amount Exceeded")
                else:
                    print("successfully debited",amt)
                    self.balance -=  amt
            else:
                print("Minimum balance should be maintained")
        else:
            print("Withdrawal limit Exceeds")
        
    def deposit(self):
        damt = int(input("Enter amount to be deposited: "))
        self.balance += damt
        print("Amount Successfully Deposited")
        
    def Exit(self):
        print("Thank you")
            
obj = ATM(1234,100000,3)       
obj.Check_pin()