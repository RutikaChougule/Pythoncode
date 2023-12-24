from random import randint
class Bank():
    def __init__(self) -> None:
        self.name=input("Enter your name:")
        self.Account_id=randint(100000,999999)
        self.phone=int(input("Enter your Phone Number:"))
        self.balance=0
    def show_info(self):
        print(f"Account number :{self.Account_id}")
        print(f"Name :{self.name}")
        print(f"Phone number:{self.phone}")
        print(f"Balance :{self.balance} \n")

    def show_balance(self):
        print(f"Account number :{self.Account_id}")
        print(f"Name :{self.name}")
        print(f"Phone number:{self.phone}")
        print(f"Balance :{self.balance} \n")
    
    def Withdraw(self):
        amount=int(input("Enter your withdraw amount:"))
        self.balance-=amount
    def deposite(self):
        amount=int(input("Enter your Deposite amount:"))
        self.balance+=amount
banks=[]
while True:
    print("1.create account")
    print("2.Show all Details")
    print("3.Deposit Amount")
    print("4.Withdraw Amout")
    print("5.For Perticular Account")
    print("6.Exit")
    Ch=int(input("Enter Your Choise:"))
    
    if Ch==1:
        obj=Bank()
        banks.append(obj)
        print(banks)
    elif Ch==2:
        if len(banks)==0:
            print("oops,Account Have Not Been created Yet!")
        else:
            for acc in banks:
                acc.show_info()
    elif Ch==3:
        if len(banks)==0:
            print("oops,Account Have Not Been created Yet!")
        else:
            acc_no=int(input("Enter Your Account Number:"))
            for ob1 in banks:
                if ob1.Account_id==acc_no: 
                    ob1.deposite()
                    break
    elif Ch==4:
        if len(banks)==0:
            print("oops,Account Have Not Been created Yet!")
        else:
            acc_no=int(input("Enter Your Account Number:"))
            for obj in banks:
                if obj.Account_id==acc_no: 
                    obj.Withdraw()
                    break
    elif Ch==5:
        if len(banks)==0:
            print("oops,Account Have Not Been created Yet!")
        else:
            print("Acoount already Created")
            acc_no=int(input("Enter Your Account Number:"))
            for s in banks:
                if s.Account_id == acc_no: 
                    s.show_balance()
                    break
    elif Ch==6:
        break
    else:
        print("Invalid Choise")
