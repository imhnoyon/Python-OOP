
with open("Message.txt",'w')as file:
    for i in range(0,3):
        file.write("I love u")
# with open("Message.txt",'a')as file:
#     for i in range(0,3):
#         file.write("I love u")

with open("Message.txt",'r')as file:
    text=file.read()
    print(text,end='')
    
