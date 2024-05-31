class calculator:
    def add(self,num1,num2):
        res=num1+num2
        print(res)
    def multiply(self,num1,num2):
        res =num1*num2
        print(res)
    def divide(self,num1,num2):
        res =num1//num2
        print(res)
    def minus(self,num1,num2):
        res =num1-num2
        print(res)
    

my_object = calculator()
my_object.add(20,10)
my_object.multiply(20,10)
my_object.divide(20,10)
my_object.minus(20,10)