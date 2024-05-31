from Order import Order
from restaurent import Restaurant
from foodItem import FoodItem
from users import Admin,Customer,Employee,user

Mamas=Restaurant("Mamas")
def Customer_menu():
    name=input("Enter Your Name : ")
    Email =input("Enter Your Email : ")
    phone = int(input("Enter Your Phone Number : "))
    Address =input("Enter Your Address : ")

    customer = Customer(name,Email,phone,Address)

  
    while True:
        print(f'MR. {customer.name} Welcome to our shop...')
        print("1.View Menu")
        print("2.Add Item to Cart")
        print("3.View Cart")
        print("4.PayBill")
        print("5.Exit")
        
        
        Option = int(input("Enter Your choice: "))
        if Option==1:
            customer.view_menu(Mamas)

        elif Option == 2:
            item_name=input("Enter Your Item : ")
            quantity=int(input("Enter Quantity : "))
            customer.Add_to_cart(Mamas,item_name,quantity)

        elif Option==3:
            customer.view_cart()

        elif Option==4:
            customer.PayBill()
        
        elif Option==5:
            break
        else:
            print("Invalid Option..!")




def Admin_menu():
    name=input("Enter Your Name : ")
    Email =input("Enter Your Email : ")
    phone = int(input("Enter Your Phone Number : "))
    Address =input("Enter Your Address : ")

    ad = Admin(name,Email,phone,Address)


    while True:
        print(f'MR. {ad.name} Welcome to our shop...')
        print("\n1.Add New Item")
        print("2.Add New Employee")
        print("3.View Employee")
        print("4.View Item")
        print("5.Delete Item")
        print("6.Exit")

        

        Option = int(input("Enter Your choice: "))

        if Option==1:
            Name=input("Enter New Item Name : ")
            price=int(input("Enter Item Price : "))
            quantity=int(input("Item Quantity : "))
            item=FoodItem(Name,price,quantity)
            ad.add_manu(Mamas,item)

        elif Option == 2:
            
            name=input("Enter Employee Name :")
            email=input("Employee Email : ")
            age=int(input("Enter Employee Ages : "))
            phone=input("Enter Employee Phone_number : ")
            salary = int(input("Employee Salary : "))
            designation=input("Employee Designation : ")
            Address=input("Enter Employee Address : ")
            employee = Employee(name, phone, email,Address,age,designation,salary)
            ad.Add_employee(Mamas,employee)



        elif Option==3:
            ad.Display_Employee(Mamas)
            

        elif Option==4:
            ad.View_menu(Mamas)
            
        
        elif Option==5:
            item_name=input("Enter item name you wanted to Deleted : ")
            ad.remove_item(Mamas,item_name)

        elif Option==6:
            break
        else:
            print("Invalid Option..!")




while True:
    print("\n\n***********Welcome to Our Restaurent Managment System***********")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")

    option = int(input("Enter your Choice: "))

    if option==1:
     Customer_menu()
    elif option==2:
        Admin_menu()
    elif option==3:
        break
    else:
        print("Invalid Option..!")



