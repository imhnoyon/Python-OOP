
from abc import ABC
from Order import Order
class user(ABC):
    def __init__(self,name,phone, email,address) -> None:
        self.name=name
        self.phone = phone
        self.email=email
        self.address=address

class Employee(user):
    def __init__(self,name,phone,email,address,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name,phone,email,address)


class Admin(user):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        
    def Add_employee(self,Restaurant,employee):
        Restaurant.Add_employee(employee)

    def Display_Employee(self,Restaurant):
        Restaurant.Display_Employee()

    def add_manu(self,Restaurant,item):
        Restaurant.Menu.Add_menu_item(item)
   
    def remove_item(self,Restaurant,item):
        Restaurant.Menu.remove_item(item)

    def View_menu(self,Restaurant):
        Restaurant.Menu.show_Menu()


    
class Customer(user):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.Cart=Order()

    def view_menu(self,Restaurant):
        Restaurant.Menu.show_Menu()

    def Add_to_cart(self,Restaurant,item_name,quantity):
        # Restaurant.Menu.show_Menu()
        item = Restaurant.Menu.find_item(item_name)
        # print(f'{item_name} jkkdjj{item}')
        if  item:
            if quantity > item.quantity:
                print("Item Quantity exceeded..!!")
            else:
                item.quantity =quantity
                self.Cart.add_item(item)
                print("Item Added..!")
        else:
            print("Item not found..!")

    def view_cart(self):
        print("******View Cart********")
        print("Name\tPrice\tQuantity")
        for item ,quantity in self.Cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')

        print(f"Total price: {self.Cart.total_price()}")

    def PayBill(self):
        print(f'Total {self.Cart.total_price()}Taka Paid Successfully..')
        self.Cart.clear()


            
