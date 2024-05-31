number =[10,20,30,40]
number.append(50)
print(number)
number.insert(1,60)
print(number)

if 50 in number:
    number.remove(50)
print(number)

last=number.pop()
print(last,number)