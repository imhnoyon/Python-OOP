from Menu import Menu
class Restaurant():
    def __init__(self,name):
        self.name=name
        self.employees =[] # data base hisabe kaj korbe
        self.Menu = Menu()


    def Add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added succesfully...!')
        

    def Display_Employee(self):
        print("Name\tPhone\tEmail\tAddress\tAges\tDesignation\tSalary")
        for emp in self.employees:
            print(f'{emp.name}\t{emp.phone}\t{emp.email}\t{emp.address}\t{emp.age}\t{emp.designation}\t{emp.salary}')
