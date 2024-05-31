String = input()
L_count=0
R_count=0
Array=[]
Array2 =''
for char in String:
    Array2 +=char
    if char == 'L':
        L_count +=1
    elif char == 'R':
        R_count +=1
    if L_count ==R_count:
        Array.append(Array2)
        L_count=0
        R_count=0
        Array2=''

print(len(Array))
for res in Array:
    print(res)