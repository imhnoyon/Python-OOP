class phone:
    # constraction
    def __init__(self,Name,Brand,price):
        self.Name=Name
        self.Brand = Brand
        self.price=price
    def call(self):
        print("Thank Your...")

My_object = phone("Mahedi","Samsung",22000)
print(My_object.Name,My_object.Brand,My_object.price)

Mahedi =phone('Mahdi','Redmi',80000)
print(Mahedi.Name,Mahedi.Brand,Mahedi.price)
Mahedi.call()
        