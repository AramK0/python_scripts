
class Bank():

    def __init__(self, balance):
        self.balance = balance
        


    def make_account(self):
            
            self.accounts = {"username" : "null", 
                             "password": "null"}
            
            self.accounts['username'] = input("Enter your name: ")
            self.accounts['password'] = input("Enter passcode: ")
            
            print(f"Hello {self.accounts['username']} You passcode is: {self.accounts['password']}")
    
    

    def check_balance(self):
        self.name = input('Enter your name: ')
        self.password = input('Enter your passcode: ')
        if(self.name == self.accounts['username'] and self.password == self.accounts['password']):
            print()
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid username or password")


    def deposit(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your passcode: ")
        if(self.name == self.accounts['username'] and self.password == self.accounts['password']):
            self.amount = int(input("Enter amount to be deposited: "))
            if(self.amount >= 0):
                self.balance += self.amount
                print(f"Your new balance is: {self.balance}")
            else:
                print("Invalid amount")
        else:
            print("Invalid username or password")

    def withdraw(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your passcode: ")
        if(self.name == self.accounts['username'] and self.password == self.accounts['password']):
            self.amount = int(input("Enter amount to be withdrawn: "))
            if(self.amount < self.balance):
                self.balance -= self.amount
                print(f"Your new balance is: {self.balance}")
            else:
                print("Invalid amount")
        else:
            print("Invalid username of password")



acc1 = Bank(50)

is_running = True

while(is_running):
    print("Welcome to the Bank")
    choice = int(input("Choose an option: 1-create account 2-check balance 3-deposit 4-withdraw 5-quit: "))

    if(choice == 1):
        acc1.make_account()
    elif(choice == 2):
        acc1.check_balance()
    elif(choice == 3):
        acc1.deposit()
    elif(choice == 4):
        acc1.withdraw()
    elif(choice == 5):
        print("Goodbye!")
        is_running = False
    else:
        print("Invalid Input")
