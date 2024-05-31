from datetime import datetime


class RideSharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders =[]
        self.drivers = []
        self.rides=[]

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __str__(self) -> str:
        return f"Company_Name : {self.company_name} with riders : {len(self.riders)} and driver : {len(self.drivers)}"
        

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time=None
        self.end_time=None
        self.estimated_fare = None


    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet -=self.estimated_fare
        self.driver.wallet +=self.estimated_fare


    def __repr__(self):
        return f'Rider details Started {self.start_location} to {self.end_location}'
        


class Ride_Request:
    def __init__(self,rider,end_location) -> None:
        self.rider = rider
        self.end_location = end_location

    
class Ride_matching:
    def __init__(self,driver) -> None:
        self.available_driver = driver

    def find_driver(self,ride_request):
        if len(self.available_driver)>0:
            print("Looking for Driver...")
            driver = self.available_driver[0]
            ride = Ride(Ride_Request.rider.current_location,ride_request.end_location)
            driver.accept_request(ride)
            return ride
        
        



        