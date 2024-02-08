class Account:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self):
        self.plus = int(input())
        self.balance += self.plus
        print(self.balance)
    def withdraw(self):
        self.minus = int(input())
        if self.minus > self.balance :
            print("Not enough money")
        else:
            self.balance -= self.minus
            print(self.balance)

balance = int(input())
owner = input()
x = Account(balance, owner)
x.deposit()
x.withdraw()