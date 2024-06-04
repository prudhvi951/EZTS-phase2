class detail:
    def __init__(self,data):
        self.data= data
        self.account = {}
        print(self.account.values)
    
class bank:
    def __init__(self,accname,accno,pas):
        self.acname = accname
        self.accno = accno
        self.pas = pas
        self.bal = 0
        self.atmno = 858544992224
        print("Accoount sucessfuly Created")
    def Debitcard(self):
        if self.acname:
            print("Your Card number is: 858544992224")
            print("Your Pin is :{}".format(self.pinno))
        else:
            print("Create the account")
    def Deposit(self,acno,pa):
        if self.accno == acno and self.pas == pa:
            n = int(input("Enter the amount to deposit: "))
            if n > 0:
                self.bal +=n
        else:
            print("Your account not found please creat your account")
            
            
    def withdraw(self,atm,pin):
         if self.atmno == atm and self.pinno == pin:
            n = int(input("Enter the amount to Withdraw: "))
            if self.bal > n:
                self.bal -=n
                print("Withdrawl Success")
            else:
                print("Less amount in your bank")
    def displayBalance(self):
        if self.bal == 0:
            print("Account not created or Zero balance")
        else:
            print("Your Acc Bal is: {}".format(self.bal))
while True:
    print("1.Create Account")
    print("2.Know your Cardno and pin")
    print("3.Deposit Money")
    print("4.Withdraw Money")
    print("5.Display Accbalance")
    print("6.Exit")
    k = int(input("Enter Your Choice: "))
    if k == 1:
        name = input("Enter Your Full Name: ")
        accno = int(input("Enter New Acc No: "))
        pa = int(input("Enter a password: "))
        a = bank(name,accno,pa)
        b = detail("sbi")
        b.account[name]=a
        
        
        
    elif k == 2:
        new.Debitcard()
    elif k == 3:
        acno = int(input("Enter Your acc no: "))
        pas = int(input("Enter your acc password: "))
        new.Deposit(acno,pas)
    elif k == 4:
        cano = int(input("Enter Your Atm no: "))
        pin = int(input("Enter your Pin: "))
        new.withdraw(cano,pin)
    elif k == 5:
        new.displayBalance()
    elif k == 6:
        print("Exiting....")
        print("....")
        break
    else:
        print("Enter a valid choice")
