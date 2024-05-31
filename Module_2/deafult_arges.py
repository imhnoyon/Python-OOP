# num of parameter pathabo,and number prothom 2ta mendatory

def Noyon(num1,num2,*number):
    print(number)
    sum=0
    for i in number:
        
        print(i)
        sum +=i
    return sum
        


Total=Noyon(10,20,30,40,50)
print("Total sum: ",Total)