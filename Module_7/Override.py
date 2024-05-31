class person:
    def __init__(self,Name,age,height,weight) -> None:
        self.Name=Name
        self.age=age
        self.height=height
        self.weight=weight

    def eat(self):
        print('vat  khai')

class cricketer(person):
     def __init__(self, Name, age, height, weight,team) -> None:
         self.team=team
         super().__init__(Name, age, height, weight)
        
     def eat(self):
        print('kichu  khai na')
    
     
    


musfiq = cricketer('Musfiqur Rahim',37,60,85,'Bangladesh')
musfiq.eat()