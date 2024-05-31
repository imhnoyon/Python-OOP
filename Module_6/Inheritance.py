# base class,parent class ,common attibute + functionality class
# derived class, child class ,uncommon attibute + functionality class

class gadet:
    def __init__(self,brand,price,color,country) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.country=country
    
    def run(self):
        print(f'Running the program')
    

class laptop:
    def __init__(self,Memory,ssd) -> None:
        self.Memory=Memory
        self.ssd=ssd

class phone(gadet):
    def __init__(self,brand ,price,color,country,dual_sim) -> None:
        self.dual_sim=dual_sim
        
        super().__init__(brand,price,color,country)

    def __repr__(self) -> str:
        return f'{self.brand} {self.price} {self.color}'


class camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel

        

my_phone=phone("samsung",120000,"red","Bangladesh","dual sim")
print(my_phone)
        
