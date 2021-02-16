# -------------------   Real time example for Method overloading---------------------
class BankAccount:
    def __init__(self,balance=10000):
        self.balance=balance
    def deposite(self,value):
        self.balance=self.balance+value
        print('The current balance is: ',self.balance)
    def withdraw(self,value):
        self.balance=self.balance-value
        print('The current balance is: ',self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,balance=10000):
        self.balance=balance
    def deposite(self, value):
        self.balance=self.balance+(value*1.03)
        print('The current balance in savings account is: ',self.balance)

class CurrentAccount(BankAccount):
    def __init__(self,balance=10000):
        self.balance=balance
    def withdraw(self,value):
        if value>1000:
            print('You can withdraw lessthan 1000 only')
        else:
            self.balance=self.balance-value
            print('You current amount in current account is', self.balance)

SA=SavingsAccount()
CA=CurrentAccount()

while True:
    print('1.Savings Account')
    print("2.Current Account")
    MOption=int(input('Please select the account type: '))
    if MOption==1:
        print('1.Withdraw')
        print('2.Deposite')
        SOption=int(input('Please select any operation type: '))
        if SOption==1:
            value=int(input('Please enter amout to withdraw from savings account: '))
            SA.withdraw(value)
        elif SOption==2:
            value=int(input('Please enter amount to deposite in savings account: '))
            SA.deposite(value)
        else:
            print('You entered ',SOption,'Its invalid operatoion')
    
    elif MOption==2:
        print('1.Withdraw')
        print('2.Deposite')
        SOption=int(input('Please select any operation type: '))
        if SOption==1:
            value=int(input('Please enter amount to withdraw from current account: '))
            CA.withdraw(value)
        elif SOption==2:
            value=int(input('Please enter amount to deposite in current account: '))
            CA.deposite(value)
        else:
            print('You entered ',SOption,'Its invalid operatoion')
    else:
        print('You entered ',MOption,'Its invalid Account Type')
#break #this example is done without break statement