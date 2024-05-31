
class bank:
    def __init__(self,Name,Initial_Balance) -> None:
        self.Name=Name
        self.__balance = Initial_Balance
        self._brance='bannai 11'

    def diposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    



obj=bank("Mahedi",1000)
print(obj.Name)
obj.diposit(40000)
print(obj.get_balance())
print(obj._brance)