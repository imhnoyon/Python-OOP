
from abc import ABC
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



class Restaurant():
    def __init__(self,name):
        self.name=name
        self.employees =[] # data base hisabe kaj korbe
        self.Menu = Menu()


    def Add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added succesfully...!')
        

    def Display_Employee(self):
        print("Employee List: ")
        for emp in self.employees:
            print(emp.name,emp.phone,emp.email,emp.address,emp.age,emp.designation,emp.salary)



class Menu:
    def __init__(self):
        self.items = [] # item er data base

    def Add_menu_item(self,item):
        self.items.append(item)


    def find_item(self,item_name):
        print(self.items[0].name)
        for item in self.items:
           
            if item.name.lower() == item_name.lower():
                return item
        
                
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item delected Successfully..!")
        else:
            print("Item not found..!")

    def show_Menu(self):
        print("Menu\tprice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class FoodItem():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity




class Order:
    def __init__(self) -> None:
        self.items={}


    def add_item(self,item):
        if item in self.items:
            self.items[item] +=item.quantity

        else:
            self.items[item] =item.quantity

    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    def clear(self):
        self.items={}            
        

                

mamas = Restaurant("mamas")
mn = Menu()
item =FoodItem("pizza",30,30)
item2 =FoodItem("Burger",50,20)
ad = Admin("Mahedi",224555,"mahedi@gmail.com","Dhaka")
ad.add_manu(mamas,item)
ad.add_manu(mamas,item2)
# mn.show_Menu()
Customer1 = Customer("noyon",454545,"h@gamil.com","Dhaka")
Customer1.view_menu(mamas)
item_name = input("Item name: ")
quantity = int(input("Item Quantity: "))


Customer1.Add_to_cart(mamas,item_name,quantity)
Customer1.view_cart()
