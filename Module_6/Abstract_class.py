
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        print('eating banana')
    def move(self):
        pass
   

class monkey(animal):
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()
    def eat(self):
        print("eat rice")
    def move(self):
        print("ami jabo")

layka=monkey('Lucky')
print(layka.name)
layka.eat()
layka.move()