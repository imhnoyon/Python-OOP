# Multi-level inheritance

class vehicle:
    def __init__(self,Name,price) -> None:
        self.Name=Name
        self.price=price

    def __repr__(self) -> str:
        return f'{self.Name} {self.price}'

class bus(vehicle):
    def __init__(self, Name, price,seat) -> None:
        self.seat=seat
        super().__init__(Name, price)
    def __repr__(self) -> str:
        return super().__repr__()

class AcBus(bus):
    def __init__(self, Name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(Name, price, seat)
    def __repr__(self) -> str:
        print(self.seat , self.temperature)
        return super().__repr__()

class track(vehicle):
    def __init__(self, Name, price,weight) -> None:
        self.weight=weight
        super().__init__(Name, price)
        


MiniBus = AcBus("Green_line",5000000,25,15)
print(MiniBus)