N = int(input())
arr = list(map(int, input().split()))
count =0
even=True
while even:
    for num in range(N):
        if arr[num] % 2 ==1:
            even=False
            break
        elif arr[num] % 2==0:
            arr[num] //= 2

    if even==True:
        count +=1
print(count)



         


        
 
    
    
     


    
        

