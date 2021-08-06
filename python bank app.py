
# welcome()


#BANK ASSIGNMENT

users = []
balance = 0




class bankdashboard():


    def __init__(self, depname, amount, pin, transname, remainder,  bills, next):
        depname, amount, pin, transname, remainder,
        bills, next

    def refresh(self):

        self.next = input("Press 1 if you would like to do another transaction or 2 to exit: ")
        if self.next == "1":
            self.dash()
        elif self.next == "2":
            print("thank you for banking with us")
            exit()
    def dash(self):
        print("\t\t\t\t\tWELLCOME TO YOUR DASHBOARD")
        print(f"{'your bank details are'}{users}")
        self.depname = input(
            "press 1 to deposit, 2 to transfer, 3 to withdraw, 4 to pay bills, 5 to recharge, 6 to exit: ")

        if self.depname == "1":
            self.deposit(balance)
        elif self.depname == "2":
            self.transfer(balance)
        elif self.depname == "3":
            self.withdraw(balance)
        elif self.depname == "4":
            self.paybills(balance)
        elif self.depname == "5":
            self.recharge(balance)
        else:
            exit()


    def deposit(self, a):
        print("DEPOSIT FORM")
        self.depname = input("enter account number: ")
        self.amount = int(input("enter amount: "))
        self.pin = input("enter your 4 digit number: ")
        if self.depname not in users:
            print("user not found")
            self.refresh()
        elif self.pin not in users:
            print("invalid pin")
            self.refresh()

        else:
            a += self.amount
            print(f"{a} {'has been deposited to your account'}")
            self.refresh()



    def transfer(self, a):
        print("TRANSFER FROM")
        self.transname = input("enter receivers account number here: ")
        self.depname = input('Enter account number: ')
        self.amount = int(input("enter amount to transfer: "))
        self.pin = input("enter your 4 digit number: ")
        if self.transname not in users:
            print("Receiver not a registered user")
            self.refresh()
        elif self.depname not in users:
            print("user not found")
            self.refresh()
        elif self.pin not in users:
            print("invalid pin")
            self.refresh()
        else:
            if self.amount > balance:
                print("insufficient funds")
                self.refresh()
            else:
                self.remainder = a - self.amount

            print(f"{self.amount} {'has been transferred from your account'}{'your balance is '}{self.remainder}")
            self.refresh()

    def withdraw(self, a):
        print("Withdrawal section")
        self.amount = int(input("enter amount to be withdrawn: "))
        self.pin = input("enter your 4 digit number: ")
        if self.pin not in users:
            print("invalid pin")
            self.refresh()
        else:
            if self.amount > balance:
                print("insufficient funds")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(f"{self.amount} {'has been transferred from your account'}{'your balance is '}{self.remainder}")
                self.refresh()

    def paybills(self, a):
        print("make your payments here")
        self.bills = input("press 1 for NEPA bill, 2 for Go tv bill, and 3 for water bill: ")
        if self.bills == "1":
            print("NEPA bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
                self.refresh()

        elif self.bills == "2":
            print("Go tv bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(
                    f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
                self.refresh()

        elif self.bills == "3":
            print("Water bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(
                    f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
            self.refresh()

    def recharge(self, a):
        print("Recharge section")
        import re
        self.depname = input("Input a valid phone number: ")
        self.amount = int(input("input card amount: "))
        self.pin = input("input your pin: ")
        num = r'080'
        if self.pin not in users:
            print("invalid pin")
            self.refresh()
        elif re.match(num, self.depname):
            print("valid phone number")
            self.refresh()
            self.remainder = a - self.amount
            print(f'{self.amount}{" has been deducted from your account, your account balance is "}{self.remainder}')
            self.refresh()
        else:
            print("invalid number")
            self.refresh()



class bank(bankdashboard):

    def __init__(self, num, name, email, password, transpass,):
        num
        name
        email
        password
        transpass

    def generator(self, a):
        import random
        range_start = 10 ** (a - 1)
        range_end = (10 ** a) - 1
        return random.randint(range_start, range_end)

    def mybank(self):
        print("\t\t\t\t\tWELCOME TO DON'S BANK")
        self.num = int(input("press 1 to register, press 2 to login, press 3 to exit app"))
        if self.num == 1:
            self.register()
        elif self.num == 2:
            self.login()
        elif self.num == 3:
            print('thanks for checking us out')
            exit()


    def register(self):

        print("registration page")
        self.name = input('Enter fullname: ')
        self.email = input("enter a valid email: ")
        self.password = input("enter your password: ")
        self.transpass = input("enter a 4 digit transaction password: ")
        self.num = self.generator(14)
        users.append(self.name)
        users.append(self.email)
        users.append(self.password)
        users.append(self.transpass)
        users.append(self.num)
        self.login()


    def login(self):
        print("login page")
        email2 = input("enter email: ")
        pass1 = input("enter password: ")

        if email2 in users and pass1 in users:
            print("login succefull")
            self.dash()
        else:
            print("username not found")
            self.register()


# john = bank(0,0,0,0,0)
# john.mybank()
# welcome()


#BANK ASSIGNMENT

users = []
balance = 0




class bankdashboard():


    def __init__(self, depname, amount, pin, transname, remainder,  bills, next):
        depname, amount, pin, transname, remainder,
        bills, next

    def refresh(self):

        self.next = input("Press 1 if you would like to do another transaction or 2 to exit: ")
        if self.next == "1":
            self.dash()
        elif self.next == "2":
            print("thank you for banking with us")
            exit()
    def dash(self):
        print("\t\t\t\t\tWELLCOME TO YOUR DASHBOARD")
        print(f"{'your bank details are'}{users}")
        self.depname = input(
            "press 1 to deposit, 2 to transfer, 3 to withdraw, 4 to pay bills, 5 to recharge, 6 to exit: ")

        if self.depname == "1":
            self.deposit(balance)
        elif self.depname == "2":
            self.transfer(balance)
        elif self.depname == "3":
            self.withdraw(balance)
        elif self.depname == "4":
            self.paybills(balance)
        elif self.depname == "5":
            self.recharge(balance)
        else:
            exit()


    def deposit(self, a):
        print("DEPOSIT FORM")
        self.depname = int(input("enter account number: "))
        self.amount = int(input("enter amount: "))
        self.pin = input("enter your 4 digit number: ")
        if self.depname not in users:
            print("user not found")
            self.refresh()
        elif self.pin not in users:
            print("invalid pin")
            self.refresh()

        else:
            a += self.amount
            print(f"{a} {'has been deposited to your account'}")
            self.refresh()



    def transfer(self, a):
        print("TRANSFER FROM")
        self.transname = input("enter receivers account number here: ")
        self.depname = input('Enter account number: ')
        self.amount = int(input("enter amount to transfer: "))
        self.pin = input("enter your 4 digit number: ")
        if self.transname not in users:
            print("Receiver not a registered user")
            self.refresh()
        elif self.depname not in users:
            print("user not found")
            self.refresh()
        elif self.pin not in users:
            print("invalid pin")
            self.refresh()
        else:
            if self.amount > balance:
                print("insufficient funds")
                self.refresh()
            else:
                self.remainder = a - self.amount

            print(f"{self.amount} {'has been transferred from your account'}{'your balance is '}{self.remainder}")
            self.refresh()

    def withdraw(self, a):
        print("Withdrawal section")
        self.amount = int(input("enter amount to be withdrawn: "))
        self.pin = input("enter your 4 digit number: ")
        if self.pin not in users:
            print("invalid pin")
            self.refresh()
        else:
            if self.amount > balance:
                print("insufficient funds")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(f"{self.amount} {'has been transferred from your account'}{'your balance is '}{self.remainder}")
                self.refresh()

    def paybills(self, a):
        print("make your payments here")
        self.bills = input("press 1 for NEPA bill, 2 for Go tv bill, and 3 for water bill: ")
        if self.bills == "1":
            print("NEPA bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
                self.refresh()

        elif self.bills == "2":
            print("Go tv bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(
                    f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
                self.refresh()

        elif self.bills == "3":
            print("Water bill")
            self.amount = int(input("enter amount: "))
            if self.amount > a:
                print("insufficient funds: ")
                self.refresh()
            else:
                self.remainder = a - self.amount
                print(
                    f'{self.amount}{" has been deducted from your account for NEPA bill, your account balance is "}{self.remainder}')
            self.refresh()

    def recharge(self, a):
        print("Recharge section")
        import re
        self.depname = input("Input a valid phone number: ")
        self.amount = int(input("input card amount: "))
        self.pin = input("input your pin: ")
        num = r'080'
        if self.pin not in users:
            print("invalid pin")
            self.refresh()
        elif re.match(num, self.depname):
            print("valid phone number")
            self.refresh()
            self.remainder = a - self.amount
            print(f'{self.amount}{" has been deducted from your account, your account balance is "}{self.remainder}')
            self.refresh()
        else:
            print("invalid number")
            self.refresh()



class bank(bankdashboard):

    def __init__(self, num, name, email, password, transpass,):
        num
        name
        email
        password
        transpass

    def generator(self, a):
        import random
        range_start = 10 ** (a - 1)
        range_end = (10 ** a) - 1
        return random.randint(range_start, range_end)

    def mybank(self):
        print("\t\t\t\t\tWELCOME TO DON'S BANK")
        self.num = int(input("press 1 to register, press 2 to login, press 3 to exit app"))
        if self.num == 1:
            self.register()
        elif self.num == 2:
            self.login()
        elif self.num == 3:
            print('thanks for checking us out')
            exit()


    def register(self):

        print("registration page")
        self.name = input('Enter fullname: ')
        self.email = input("enter a valid email: ")
        self.password = input("enter your password: ")
        self.transpass = input("enter a 4 digit transaction password: ")
        self.num = self.generator(6)
        users.append(self.name)
        users.append(self.email)
        users.append(self.password)
        users.append(self.transpass)
        users.append(self.num)
        self.login()


    def login(self):
        print("login page")
        email2 = input("enter email: ")
        pass1 = input("enter password: ")

        if email2 in users and pass1 in users:
            print("login succefull")
            self.dash()
        else:
            print("username not found")
            self.register()


john = bank(0,0,0,0,0)
john.mybank()