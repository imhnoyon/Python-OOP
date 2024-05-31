
from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0


    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    


class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount) -> None:
        super().__init__(name, email, nid)
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location

    def display_profile(self):
        print(f'Rider_Name : {self.name} And Email : {self.email}')

    def load_cash(self,amount):
        if amount > 0:
            self.wallet +=amount
        else:
            print("Amount less than 0.")

    def update_location(self,current_location):
        self.current_location=current_location

    def request_ride(self,ride_sharing,destination):
        pass

    def show_current_ride(self):
        print(self.current_ride)




class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet=0


    def display_profile(self):
        print("Driver_Name : {self.name}")

    def accept_ride(self,ride):
        #accept korbo
        ride.set_driver(self)


    
