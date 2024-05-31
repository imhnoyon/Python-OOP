class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=20000

    def current_balance(self):
        self.balance

    def diposit(self,amount):
        if amount > 0:
            self.balance +=amount
            print(self.balance)

    def withdraw(self,amount):
        if self.min_withdraw > amount:
            print(f'you cannot withdraw.you can minimum withdraw:{self.min_withdraw}')
        elif self.max_withdraw < amount:
            print(f'Miximum limit:{self.max_withdraw}')
        else:
            self.balance -=amount
            print(f'Here is your money:{amount}')
            print(f'withdrawing after balance:{self.balance}')

islamic=bank(25000)

islamic.diposit(10000)
islamic.withdraw(19000)
