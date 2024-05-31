number =[10,50,30,999,951,40,90,20,150,654]
odds=[]
for num in number:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)


players =['Sakib','Musfik','Mustafiz']
ages = [38,35,32]
list=[]
for player in players:
    for age in ages:
        list.append([player,age])



print(list)
   


numbers =[7,6,5,3,3,2,1]
print(numbers[-4])