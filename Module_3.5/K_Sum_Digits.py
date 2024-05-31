
N=int(input())

number = int(input())
# print(Array)
sum=0

while number > 0:
    b=number%10
    sum +=b
    number=number // 10
   

print(sum)


