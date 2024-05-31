from ride import RideSharing,Ride_Request,Ride,Ride_matching
from user import User,Rider,Driver
from vehicle import Vehicle,Car,Bike

Pathao = RideSharing("Pathao")
Mahedi = Rider('Mahedi Hasan Noyon','noyon@gmail.com',10350400,'Uttara',1000)
Pathao.add_rider(Mahedi)
Hasan = Driver('Hasan','hasan@gmail.com',12245,'Uttara')
Pathao.add_driver(Hasan)
print(Pathao)